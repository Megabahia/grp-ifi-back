from .models import PreAprobados, ArchivosFirmados
from ..corp_empresas.models import Empleados
from ..corp_creditoPersonas.models import CreditoPersonas
from .serializers import (
    CreditoArchivosSerializer,
    ArchivosFirmadosSerializer,
)
from ..corp_creditoPersonas.serializers import CreditoPersonasSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.conf import settings
from apps.config import config
# Importar boto3
import boto3
import tempfile
import environ
import os
# importar clase json
import json
# Importar producer
from .producer import publish
# Sumar Fechas
from datetime import datetime
from datetime import timedelta
# Enviar Correo
from apps.config.util import sendEmail
# Generar codigos aleatorios
import string
import random
# excel
import openpyxl
# ObjectId
from bson import ObjectId
# logs
from apps.CENTRAL.central_logs.methods import createLog, datosTipoLog, datosProductosMDP
# Importar en producer de los creditos personas
from ..corp_creditoPersonas.producer_ifi import publish as publish_credit

# declaracion variables log
datosAux = datosProductosMDP()
datosTipoLogAux = datosTipoLog()
# asignacion datos modulo
logModulo = datosAux['modulo']
logApi = datosAux['api']
# asignacion tipo de datos
logTransaccion = datosTipoLogAux['transaccion']
logExcepcion = datosTipoLogAux['excepcion']


# CRUD
# CREAR
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def creditoArchivos_create(request):
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi + 'create/',
        'modulo': logModulo,
        'tipo': logExcepcion,
        'accion': 'CREAR',
        'fechaInicio': str(timezone_now),
        'dataEnviada': '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida': '{}'
    }
    if request.method == 'POST':
        try:
            logModel['dataEnviada'] = str(request.data)
            request.data['created_at'] = str(timezone_now)
            if 'updated_at' in request.data:
                request.data.pop('updated_at')

            serializer = CreditoArchivosSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                createLog(logModel, serializer.data, logTransaccion)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            createLog(logModel, serializer.errors, logExcepcion)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            err = {"error": 'Un error ha ocurrido: {}'.format(e)}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def creditoArchivos_list(request):
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi + 'list/',
        'modulo': logModulo,
        'tipo': logExcepcion,
        'accion': 'LEER',
        'fechaInicio': str(timezone_now),
        'dataEnviada': '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida': '{}'
    }
    if request.method == 'POST':
        try:
            logModel['dataEnviada'] = str(request.data)
            # paginacion
            page_size = int(request.data['page_size'])
            page = int(request.data['page'])
            offset = page_size * page
            limit = offset + page_size
            # Filtros
            filters = {"state": "1"}

            if "minimoCarga" in request.data:
                if request.data["minimoCarga"] != '':
                    filters['fechaCargaArchivo__gte'] = str(request.data["minimoCarga"])

            if "maximoCarga" in request.data:
                if request.data["maximoCarga"] != '':
                    filters['fechaCargaArchivo__lte'] = str(request.data["maximoCarga"])

            if "minimoCreacion" in request.data:
                if request.data["minimoCreacion"] != '':
                    filters['created_at__gte'] = str(request.data["minimoCreacion"])

            if "maximaCreacion" in request.data:
                if request.data["maximaCreacion"] != '':
                    filters['created_at__lte'] = datetime.strptime(request.data['maximaCreacion'],
                                                                   "%Y-%m-%d").date() + timedelta(days=1)

            if "user_id" in request.data:
                if request.data["user_id"] != '':
                    filters['user_id'] = str(request.data["user_id"])

            if "campania" in request.data:
                if request.data["campania"] != '':
                    filters['campania'] = str(request.data["campania"])

            if "tipoCredito" in request.data:
                if request.data["tipoCredito"] != '':
                    filters['tipoCredito'] = str(request.data["tipoCredito"])

            # Serializar los datos
            query = PreAprobados.objects.filter(**filters).order_by('-created_at')
            serializer = CreditoArchivosSerializer(query[offset:limit], many=True)
            new_serializer_data = {'cont': query.count(), 'info': serializer.data}
            # envio de datos
            return Response(new_serializer_data, status=status.HTTP_200_OK)
        except Exception as e:
            err = {"error": 'Un error ha ocurrido: {}'.format(e)}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST)


# ELIMINAR
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def creditoArchivos_delete(request, pk):
    nowDate = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi + 'delete/',
        'modulo': logModulo,
        'tipo': logExcepcion,
        'accion': 'BORRAR',
        'fechaInicio': str(nowDate),
        'dataEnviada': '{}',
        'fechaFin': str(nowDate),
        'dataRecibida': '{}'
    }
    try:
        try:
            query = PreAprobados.objects.filter(pk=pk, state=1).first()
        except PreAprobados.DoesNotExist:
            err = {"error": "No existe"}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_404_NOT_FOUND)
            return Response(status=status.HTTP_404_NOT_FOUND)
        # tomar el dato
        if request.method == 'DELETE':
            serializer = CreditoArchivosSerializer(query, data={'state': '0', 'updated_at': str(nowDate)}, partial=True)
            if serializer.is_valid():
                serializer.save()
                createLog(logModel, serializer.data, logTransaccion)
                return Response(serializer.data, status=status.HTTP_200_OK)
            createLog(logModel, serializer.errors, logExcepcion)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        err = {"error": 'Un error ha ocurrido: {}'.format(e)}
        createLog(logModel, err, logExcepcion)
        return Response(err, status=status.HTTP_400_BAD_REQUEST)

    # METODO SUBIR ARCHIVOS EXCEL


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def uploadEXCEL_creditosPreaprobados(request, pk):
    contValidos = 0
    contInvalidos = 0
    contTotal = 0
    errores = []
    try:
        if request.method == 'POST':
            archivo = PreAprobados.objects.filter(pk=pk, state=1).first()
            # environ init
            env = environ.Env()
            environ.Env.read_env()  # LEE ARCHIVO .ENV
            client_s3 = boto3.client(
                's3',
                aws_access_key_id=env.str('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=env.str('AWS_SECRET_ACCESS_KEY')
            )
            with tempfile.TemporaryDirectory() as d:
                ruta = d + 'creditosPreAprobados.xlsx'
                s3 = boto3.resource('s3')
                s3.meta.client.download_file('globalredpymes', str(archivo.linkArchivo), ruta)

            first = True  # si tiene encabezado
            #             uploaded_file = request.FILES['documento']
            # you may put validations here to check extension or file size
            wb = openpyxl.load_workbook(ruta)
            # getting a particular sheet by name out of many sheets
            worksheet = wb["Clientes"]
            lines = list()
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            lines.append(row_data)

        for dato in lines:
            contTotal += 1
            if first:
                first = False
                continue
            else:
                if len(dato) == 21:
                    resultadoInsertar = insertarDato_creditoPreaprobado(dato, archivo.empresa_financiera)
                    if resultadoInsertar != 'Dato insertado correctamente':
                        contInvalidos += 1
                        errores.append({"error": "Error en la línea " + str(contTotal) + ": " + str(resultadoInsertar)})
                    else:
                        contValidos += 1
                else:
                    contInvalidos += 1
                    errores.append({"error": "Error en la línea " + str(
                        contTotal) + ": la fila tiene un tamaño incorrecto (" + str(len(dato)) + ")"})

        result = {"mensaje": "La Importación se Realizo Correctamente",
                  "correctos": contValidos,
                  "incorrectos": contInvalidos,
                  "errores": errores
                  }
        os.remove(ruta)
        # archivo.state = 0
        archivo.estado = "Cargado"
        archivo.save()
        return Response(result, status=status.HTTP_201_CREATED)

    except Exception as e:
        err = {"error": 'Error verifique el archivo, un error ha ocurrido: {}'.format(e)}
        return Response(err, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def uploadEXCEL_microCreditosPreaprobados(request, pk):
    contValidos = 0
    contInvalidos = 0
    contTotal = 0
    errores = []
    try:
        if request.method == 'POST':
            archivo = PreAprobados.objects.filter(pk=pk, state=1).first()
            # environ init
            env = environ.Env()
            environ.Env.read_env()  # LEE ARCHIVO .ENV
            client_s3 = boto3.client(
                's3',
                aws_access_key_id=env.str('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=env.str('AWS_SECRET_ACCESS_KEY')
            )
            with tempfile.TemporaryDirectory() as d:
                ruta = d + 'creditosPreAprobados.xlsx'
                s3 = boto3.resource('s3')
                s3.meta.client.download_file('globalredpymes', str(archivo.linkArchivo), ruta)

            first = True  # si tiene encabezado
            #             uploaded_file = request.FILES['documento']
            # you may put validations here to check extension or file size
            wb = openpyxl.load_workbook(ruta)
            # getting a particular sheet by name out of many sheets
            worksheet = wb["Clientes"]
            lines = list()
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            lines.append(row_data)

        for dato in lines:
            contTotal += 1
            if first:
                first = False
                continue
            else:
                if len(dato) == 23:
                    resultadoInsertar = insertarDato_creditoPreaprobado(dato, archivo.empresa_financiera)
                    if resultadoInsertar != 'Dato insertado correctamente':
                        contInvalidos += 1
                        errores.append({"error": "Error en la línea " + str(contTotal) + ": " + str(resultadoInsertar)})
                    else:
                        contValidos += 1
                else:
                    contInvalidos += 1
                    errores.append({"error": "Error en la línea " + str(
                        contTotal) + ": la fila tiene un tamaño incorrecto (" + str(len(dato)) + ")"})

        result = {"mensaje": "La Importación se Realizo Correctamente",
                  "correctos": contValidos,
                  "incorrectos": contInvalidos,
                  "errores": errores
                  }
        os.remove(ruta)
        # archivo.state = 0
        archivo.estado = "Cargado"
        archivo.save()
        return Response(result, status=status.HTTP_201_CREATED)

    except Exception as e:
        err = {"error": 'Error verifique el archivo, un error ha ocurrido: {}'.format(e)}
        return Response(err, status=status.HTTP_400_BAD_REQUEST)


# METODO SUBIR ARCHIVOS EXCEL
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def uploadEXCEL_creditosPreaprobados_empleados(request, pk):
    contValidos = 0
    contInvalidos = 0
    contTotal = 0
    errores = []
    try:
        if request.method == 'POST':
            archivo = PreAprobados.objects.filter(pk=pk, state=1).first()
            # environ init
            env = environ.Env()
            environ.Env.read_env()  # LEE ARCHIVO .ENV
            client_s3 = boto3.client(
                's3',
                aws_access_key_id=env.str('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=env.str('AWS_SECRET_ACCESS_KEY')
            )
            with tempfile.TemporaryDirectory() as d:
                ruta = d + 'creditosPreAprobados.xlsx'
                s3 = boto3.resource('s3')
                s3.meta.client.download_file('globalredpymes', str(archivo.linkArchivo), ruta)

            first = True  # si tiene encabezado
            #             uploaded_file = request.FILES['documento']
            # you may put validations here to check extension or file size
            wb = openpyxl.load_workbook(ruta)
            # getting a particular sheet by name out of many sheets
            worksheet = wb["Clientes"]
            lines = list()
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            lines.append(row_data)

        for dato in lines:
            contTotal += 1
            if first:
                first = False
                continue
            else:
                if len(dato) == 23:
                    resultadoInsertar = insertarDato_creditoPreaprobado_empleado(dato, archivo.empresa_financiera)
                    if resultadoInsertar != 'Dato insertado correctamente':
                        contInvalidos += 1
                        errores.append({"error": "Error en la línea " + str(contTotal) + ": " + str(resultadoInsertar)})
                    else:
                        contValidos += 1
                else:
                    contInvalidos += 1
                    errores.append({"error": "Error en la línea " + str(
                        contTotal) + ": la fila tiene un tamaño incorrecto (" + str(len(dato)) + ")"})

        result = {"mensaje": "La Importación se Realizo Correctamente",
                  "correctos": contValidos,
                  "incorrectos": contInvalidos,
                  "errores": errores
                  }
        os.remove(ruta)
        # archivo.state = 0
        archivo.estado = "Cargado"
        archivo.save()
        return Response(result, status=status.HTTP_201_CREATED)

    except Exception as e:
        err = {"error": 'Error verifique el archivo, un error ha ocurrido: {}'.format(e)}
        return Response(err, status=status.HTTP_400_BAD_REQUEST)


# INSERTAR DATOS EN LA BASE INDIVIDUAL
def insertarDato_creditoPreaprobado(dato, empresa_financiera):
    try:
        timezone_now = timezone.localtime(timezone.now())
        data = {}
        data['vigencia'] = dato[0].replace('"', "")[0:10] if dato[0] != "NULL" else None
        data['concepto'] = dato[1].replace('"', "") if dato[1] != "NULL" else None
        data['monto'] = dato[2].replace('"', "") if dato[2] != "NULL" else None
        data['montoDisponible'] = dato[2].replace('"', "") if dato[2] != "NULL" else None
        data['plazo'] = dato[3].replace('"', "") if dato[3] != "NULL" else None
        data['interes'] = dato[4].replace('"', "") if dato[4] != "NULL" else None
        data['cuota'] = dato[5].replace('"', "") if dato[5] != "NULL" else None
        data['tipoPersona'] = dato[6].replace('"', "") if dato[6] != "NULL" else None
        data['estadoCivil'] = dato[7].replace('"', "") if dato[7] != "NULL" else None
        data['estado'] = 'Nuevo'
        data['tipoCredito'] = 'Negocio-PreAprobado'
        data['canal'] = 'Negocio-PreAprobado'
        # persona = Personas.objects.filter(identificacion=dato[5],state=1).first()
        # data['user_id'] = persona.user_id
        data['numeroIdentificacion'] = dato[8]
        data['nombres'] = dato[9].replace('"', "") if dato[9] != "NULL" else None
        data['apellidos'] = dato[10].replace('"', "") if dato[10] != "NULL" else None
        data['nombresCompleto'] = data['nombres'] + ' ' + data['apellidos']
        data['empresaIfis_id'] = empresa_financiera
        data['empresasAplican'] = dato[20]
        data['created_at'] = str(timezone_now)
        # Genera el codigo
        codigo = (''.join(random.choice(string.digits) for _ in range(int(6))))
        data['codigoPreaprobado'] = codigo
        # inserto el dato con los campos requeridos
        credito = CreditoPersonas.objects.create(**data)
        credito.external_id = credito._id
        credito.save()
        creditoSerializer = CreditoPersonasSerializer(credito, data=data, partial=True)
        enviarCodigoCorreo(codigo, monto=data['monto'], email=dato[16])
        if creditoSerializer.is_valid():
            publish_credit(creditoSerializer.data)
        return 'Dato insertado correctamente'
    except Exception as e:
        return str(e)


# INSERTAR DATOS EN LA BASE INDIVIDUAL
def insertarDato_creditoPreaprobado(dato, empresa_financiera):
    try:
        timezone_now = timezone.localtime(timezone.now())
        data = {}
        data['vigencia'] = dato[0].replace('"', "")[0:10] if dato[0] != "NULL" else None
        data['concepto'] = dato[1].replace('"', "") if dato[1] != "NULL" else None
        data['monto'] = dato[2].replace('"', "") if dato[2] != "NULL" else None
        data['montoDisponible'] = dato[2].replace('"', "") if dato[2] != "NULL" else None
        data['plazo'] = dato[3].replace('"', "") if dato[3] != "NULL" else None
        data['interes'] = dato[4].replace('"', "") if dato[4] != "NULL" else None
        data['cuota'] = dato[5].replace('"', "") if dato[5] != "NULL" else None
        data['tipoPersona'] = dato[6].replace('"', "") if dato[6] != "NULL" else None
        data['ingresosMensuales'] = dato[7].replace('"', "") if dato[7] != "NULL" else None
        data['egresosMensuales'] = dato[8].replace('"', "") if dato[8] != "NULL" else None
        data['patrimonio'] = dato[9].replace('"', "") if dato[9] != "NULL" else None

        data['rucEmpresa'] = dato[10].replace('"', "") if dato[10] != "NULL" else None
        data['razonSocial'] = dato[11].replace('"', "") if dato[11] != "NULL" else None
        data['fechaInicioActividades'] = dato[13].replace('"', "") if dato[13] != "NULL" else None
        data['email'] = dato[18].replace('"', "") if dato[18] != "NULL" else None
        data['estado'] = 'Nuevo'
        data['tipoCredito'] = 'Pymes-PreAprobado'
        data['canal'] = 'Pymes-PreAprobado'
        data['created_at'] = str(timezone_now)
        # Genera el codigo
        codigo = (''.join(random.choice(string.digits) for _ in range(int(6))))
        data['codigoPreaprobado'] = codigo
        # inserto el dato con los campos requeridos
        credito = CreditoPersonas.objects.create(**data)
        credito.external_id = credito._id
        credito.save()
        creditoSerializer = CreditoPersonasSerializer(credito, data=data, partial=True)
        enviarCodigoCorreoMicroCredito(data['razonSocial'], codigo, monto=data['monto'], email=dato[18])
        if creditoSerializer.is_valid():
            publish_credit(creditoSerializer.data)
        return 'Dato insertado correctamente'
    except Exception as e:
        return str(e)


# INSERTAR DATOS EN LA BASE INDIVIDUAL
def insertarDato_creditoPreaprobado_empleado(dato, empresa_financiera):
    try:
        timezone_now = timezone.localtime(timezone.now())
        data = {}
        data['vigencia'] = dato[0].replace('"', "")[0:10] if dato[0] != "NULL" else None
        data['concepto'] = dato[1].replace('"', "") if dato[1] != "NULL" else None
        data['monto'] = dato[2].replace('"', "") if dato[2] != "NULL" else None
        data['plazo'] = dato[3].replace('"', "") if dato[3] != "NULL" else None
        data['interes'] = dato[4].replace('"', "") if dato[4] != "NULL" else None
        data['cuota'] = dato[5].replace('"', "") if dato[5] != "NULL" else None
        data['tipoPersona'] = dato[6].replace('"', "") if dato[6] != "NULL" else None
        data['estadoCivil'] = dato[7].replace('"', "") if dato[7] != "NULL" else None
        data['estado'] = 'Nuevo'
        data['tipoCredito'] = 'Empleado-PreAprobado'
        data['canal'] = 'Empleado-PreAprobado'
        # persona = Personas.objects.filter(identificacion=dato[5],state=1).first()
        # data['user_id'] = persona.user_id
        empleado = Empleados.objects.filter(identificacion=dato[8]).first()
        if empleado is None:
            return f"Empleado {dato[9]} {dato[10]} {dato[8]} no existe"
        data['numeroIdentificacion'] = dato[8]
        data['nombres'] = dato[9].replace('"', "") if dato[9] != "NULL" else None
        data['apellidos'] = dato[10].replace('"', "") if dato[10] != "NULL" else None
        data['nombresCompleto'] = data['nombres'] + ' ' + data['apellidos']
        data['empresaIfis_id'] = empresa_financiera
        data['empresasAplican'] = dato[22]
        data['created_at'] = str(timezone_now)
        # Genera el codigo
        codigo = (''.join(random.choice(string.digits) for _ in range(int(6))))
        data['codigoPreaprobado'] = codigo
        # inserto el dato con los campos requeridos
        credito = CreditoPersonas.objects.create(**data)
        credito.external_id = credito._id
        credito.save()
        creditoSerializer = CreditoPersonasSerializer(credito, data=data, partial=True)
        enviarCodigoCorreo(codigo, monto=data['monto'], email=dato[16])
        if creditoSerializer.is_valid():
            publish_credit(creditoSerializer.data)
        return 'Dato insertado correctamente'
    except Exception as e:
        return str(e)


def enviarCodigoCorreo(codigo, monto, email):
    subject, from_email, to = 'Generacion de codigo de credito pre-aprobado', "08d77fe1da-d09822@inbox.mailtrap.io", \
                              email
    txt_content = codigo
    html_content = """
            <html>
                <body>
                    <h1>Se acaba de generar el codigo de verificación de su cuenta</h1>

                    <p>USTED TIENE UN CREDITO PRE-APROBADO DE $ """ + monto + """, PARA QUE REALICE LA COMPRA EN www.credicompra.com, 
                    Por favor ingrese a la plataforma www.credicompra.com y disfrute de su compra: <a href='www.credicompra.com'>Link</a>
                    </p>

                    <a href='""" + config.API_FRONT_END_BIGPUNTOS + """/pages/preApprovedCreditConsumer'>Link</a>

                    Al ingresar por favor digitar el siguiente código: """ + codigo + """ en la siguiente pagina<br>                    

                    Saludos,<br>
                    Equipo Global Red Pymes.<br>
                </body>
            </html>
            """
    sendEmail(subject, txt_content, from_email, to, html_content)


def enviarCodigoCorreoMicroCredito(razonSocial, codigo, monto, email):
    subject, from_email, to = 'Generacion de codigo de credito pre-aprobado', "08d77fe1da-d09822@inbox.mailtrap.io", \
                              email
    txt_content = codigo
    html_content = f"""
                <html>
                    <body>
                        <h1>Se acaba de generar el codigo de verificación de su cuenta</h1>
                        <p>{razonSocial} tienes una LINEA DE CRÉDITO PRE-APROBADO PARA PAGO A PROVEEDORES DE {monto}</p>
                        <br>
                        <p>Tu código para acceder a tu crédito pre-aprobado PARA PAGO A PROVEEDORES es: {codigo},
                         ingresa al siguiente link y registra tus datos. Crea tu cuenta: {config.API_FRONT_END_SANJOSE}
                        </p><br>
                        Saludos,<br>
                        Equipo Global Red Pymes.<br>
                    </body>
                </html>
                """
    sendEmail(subject, txt_content, from_email, to, html_content)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def creditoArchivos_subir_documentosFirmados_create(request):
    request.POST._mutable = True
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi + 'subir/documentosFirmados',
        'modulo': logModulo,
        'tipo': logExcepcion,
        'accion': 'CREAR',
        'fechaInicio': str(timezone_now),
        'dataEnviada': '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida': '{}'
    }
    if request.method == 'POST':
        try:
            logModel['dataEnviada'] = str(request.data)
            request.data['created_at'] = str(timezone_now)
            if 'updated_at' in request.data:
                request.data.pop('updated_at')

            serializer = ArchivosFirmadosSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                createLog(logModel, serializer.data, logTransaccion)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            createLog(logModel, serializer.errors, logExcepcion)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            err = {"error": 'Un error ha ocurrido: {}'.format(e)}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def creditoArchivos_ver_documentosFirmados_list(request):
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi + 'ver/documentosFirmados',
        'modulo': logModulo,
        'tipo': logExcepcion,
        'accion': 'LEER',
        'fechaInicio': str(timezone_now),
        'dataEnviada': '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida': '{}'
    }
    try:
        try:
            query = ArchivosFirmados.objects.get(numeroIdentificacion=request.data['numeroIdentificacion'], state=1)
        except ArchivosFirmados.DoesNotExist:
            err = {"error": "No existe"}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_200_OK)
        # tomar el dato
        if request.method == 'POST':
            serializer = ArchivosFirmadosSerializer(query)
            createLog(logModel, serializer.data, logTransaccion)
            return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        err = {"error": 'Un error ha ocurrido: {}'.format(e)}
        createLog(logModel, err, logExcepcion)
        return Response(err, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def creditoArchivos_ver_documentosFirmados_list_todos(request):
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi + '/documentosFirmados/listar/todos',
        'modulo': logModulo,
        'tipo': logExcepcion,
        'accion': 'LEER',
        'fechaInicio': str(timezone_now),
        'dataEnviada': '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida': '{}'
    }
    try:
        logModel['dataEnviada'] = str(request.data)
        # paginacion
        page_size = int(request.data['page_size'])
        page = int(request.data['page'])
        offset = page_size * page
        limit = offset + page_size
        # Filtros
        filters = {"state": "1"}

        # Serializar los datos
        query = ArchivosFirmados.objects.filter(**filters).order_by('-created_at')
        serializer = ArchivosFirmadosSerializer(query[offset:limit], many=True)
        new_serializer_data = {'cont': query.count(), 'info': serializer.data}
        # envio de datos
        return Response(new_serializer_data, status=status.HTTP_200_OK)
    except Exception as e:
        err = {"error": 'Un error ha ocurrido: {}'.format(e)}
        createLog(logModel, err, logExcepcion)
        return Response(err, status=status.HTTP_400_BAD_REQUEST)

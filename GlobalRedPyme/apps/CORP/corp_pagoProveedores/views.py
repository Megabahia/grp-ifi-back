from .models import PagoProveedores
from .serializers import (
    PagoProveedorSerializer
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
import json
# Enviar Correo
from apps.config.util import sendEmail
# ObjectId
from bson import ObjectId
# logs
from apps.CENTRAL.central_logs.methods import createLog, datosTipoLog, datosProductosMDP

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
def pagoProveedores_create(request):
    request.POST._mutable = True
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

            serializer = PagoProveedorSerializer(data=request.data)
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
def pagoProveedores_update(request, pk):
    request.POST._mutable = True
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi + 'update/',
        'modulo': logModulo,
        'tipo': logExcepcion,
        'accion': 'ESCRIBIR',
        'fechaInicio': str(timezone_now),
        'dataEnviada': '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida': '{}'
    }
    try:
        try:
            logModel['dataEnviada'] = str(request.data)
            query = PagoProveedores.objects.filter(pk=ObjectId(pk), state=1).first()
        except PagoProveedores.DoesNotExist:
            errorNoExiste = {'error': 'No existe'}
            createLog(logModel, errorNoExiste, logExcepcion)
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'POST':
            now = timezone.localtime(timezone.now())
            request.data['updated_at'] = str(now)
            if 'created_at' in request.data:
                request.data.pop('created_at')
            serializer = PagoProveedorSerializer(query, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                usuario = json.loads(query.usuario)
                if 'Negado' in query.estado:
                    enviarNegadoPago(usuario['email'], query.valorPagar)

                if 'Procesar' in query.estado:
                    enviarProcesandoPago(usuario['email'], query.valorPagar)

                createLog(logModel, serializer.data, logTransaccion)
                return Response(serializer.data)
            createLog(logModel, serializer.errors, logExcepcion)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        err = {"error": 'Un error ha ocurrido: {}'.format(e)}
        createLog(logModel, err, logExcepcion)
        return Response(err, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def pagoProveedores_list(request):
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

            if "empresa_id" in request.data:
                if request.data["empresa_id"] != '':
                    filters['empresa_id'] = str(request.data["empresa_id"])

            # Serializar los datos
            query = PagoProveedores.objects.filter(**filters).order_by('-created_at')
            serializer = PagoProveedorSerializer(query[offset:limit], many=True)
            new_serializer_data = {'cont': query.count(),
                                   'info': serializer.data}
            # envio de datos
            return Response(new_serializer_data, status=status.HTTP_200_OK)
        except Exception as e:
            err = {"error": 'Un error ha ocurrido: {}'.format(e)}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST)


def enviarNegadoPago(email, monto):
    subject, from_email, to = 'RAZÓN POR LA QUE SE NIEGA EL PAGO A PROVEEDORES', "08d77fe1da-d09822@inbox.mailtrap.io", \
                              email
    txt_content = monto
    html_content = f"""
                <html>
                    <body>
                        <h1>PAGO A PROVEEDORES - CRÉDITO PAGOS</h1>
                        <br>
                        <h3><b>Lo sentimos!!</b></h3>
                        <br>
                        <p>La transferencia por ${monto} DE LA FACTURA A PAGAR ha sido rechazada. 
                        Por favor revise sus fondos e intente de nuevo.</p>
                        <br>
                        <br>
                        <p>Si cree que es un error, contáctese con su agente a través de https://walink.co/b5e9c0</p>
                        <br>
                        Atentamente,
                        <br>
                        Global RedPyme – Crédito Pagos
                        <br>
                    </body>
                </html>
                """
    sendEmail(subject, txt_content, from_email, to, html_content)


def enviarProcesandoPago(email, monto):
    subject, from_email, to = 'Transferencia exitosa', "08d77fe1da-d09822@inbox.mailtrap.io", \
                              email
    txt_content = monto
    html_content = f"""
                <html>
                    <body>
                        <h1>PAGO A PROVEEDORES - CRÉDITO PAGOS</h1>
                        <br>
                        <h3><b>FELICIDADES!!</b></h3>
                        <br>
                        <p>La transferencia por ${monto} DE LA FACTURA A PAGAR ha sido realizada con éxito, 
                        adjuntamos el comprobante del pago realizado. 
                        En 24 horas será acreditado a la cuenta destino.</p>
                        <br>
                        <br>
                        Atentamente,
                        <br>
                        Global RedPyme – Crédito Pagos
                        <br>
                    </body>
                </html>
                """
    sendEmail(subject, txt_content, from_email, to, html_content)

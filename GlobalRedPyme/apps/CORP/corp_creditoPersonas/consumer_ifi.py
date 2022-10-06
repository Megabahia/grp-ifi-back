import boto3
import json
# Importar configuraciones
from apps.config import config
from .serializers import CreditoPersonasSerializer
from .models import CreditoPersonas
from bson import ObjectId
#logs
from apps.CENTRAL.central_logs.methods import createLog,datosTipoLog, datosProductosMDP
#declaracion variables log
datosAux=datosProductosMDP()
datosTipoLogAux=datosTipoLog()
#asignacion datos modulo
logModulo=datosAux['modulo']
logApi=datosAux['api']
#asignacion tipo de datos
logTransaccion=datosTipoLogAux['transaccion']
logExcepcion=datosTipoLogAux['excepcion']

def get_queue_url():
    logModel = {
        'endPoint': logApi+'listOne/',
        'modulo':logModulo,
        'tipo' : logExcepcion,
        'accion' : 'CRON_SQS_BIGBUNTOS',
        # 'fechaInicio' : str(timezone_now),
        'dataEnviada' : '{}',
        # 'fechaFin': str(timezone_now),
        'dataRecibida' : '{}'
    }
    try:
        region_name = config.AWS_REGION_NAME
        queue_name = config.AWS_QUEUE_NAME
        max_queue_messages = 10
        aws_access_key_id = config.AWS_ACCESS_KEY_ID_COLAS
        aws_secret_access_key = config.AWS_SECRET_ACCESS_KEY_COLAS
        sqs = boto3.resource('sqs', region_name=region_name,
                            aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key)
        queue = sqs.get_queue_by_name(QueueName=queue_name)
        # Consultar la cola maximo 10 mensajes
        for message in queue.receive_messages(MaxNumberOfMessages=max_queue_messages):
            # process message body
            body = json.loads(message.body)
            jsonRequest = json.loads(body['Message'])
            _idCredidPerson = json.loads(body['Message'])['_id']
            jsonRequest['external_id'] = _idCredidPerson
            # Por el momento crea los nuevos registros que llegan sqs
            query = CreditoPersonas.objects.filter(external_id=_idCredidPerson, state=1).first()
            print('jsonRequest', jsonRequest)
            if query is None:
                # Quitar los campos que no estan en el modelo de credito persona
                jsonRequest.pop('whatsappPersona')
                jsonRequest.pop('emailPersona')
                jsonRequest['estado'] = 'Nuevo'
                print('antes de guardar')
                CreditoPersonas.objects.create(**jsonRequest)
                print('se guardo')
            else:
                # Quitar los campos que no estan en el modelo de credito persona
                jsonRequest.pop('whatsappPersona')
                jsonRequest.pop('emailPersona')

                print('antes de actualizar')
                CreditoPersonas.objects.update(**jsonRequest)
                print('se guardo')

                # query.numero=jsonRequest['numero']
                # query.canal=jsonRequest['canal']
                # query.monto=jsonRequest['monto']
                # query.plazo=jsonRequest['plazo']
                # query.aceptaTerminos=jsonRequest['aceptaTerminos']
                # query.estado=jsonRequest['estado']
                # query.user_id=jsonRequest['user_id']
                # query.empresaComercial_id=jsonRequest['empresaComercial_id']
                # # query.empresaIfis_id=jsonRequest['empresaIfis_id']
                # query.reporteBuro=reporteBuro
                # query.calificacionBuro=jsonRequest['calificacionBuro']
                # query.buroValido=jsonRequest['buroValido']
                # query.identificacion=identificacion
                # query.ruc=ruc
                # query.rolesPago=rolesPago
                # query.panillaIESS=panillaIESS
                # query.tomarSolicitud=jsonRequest['tomarSolicitud']
                # query.fechaAprobacion=jsonRequest['fechaAprobacion']
                # query.tipoCredito=jsonRequest['tipoCredito']
                # query.concepto=jsonRequest['concepto']
                # query.documentoAprobacion=documentoAprobacion
                # query.empresasAplican=jsonRequest['empresasAplican']
                # query.vigencia=jsonRequest['vigencia']
                # query.interes=jsonRequest['interes']
                # query.nombres=jsonRequest['nombres']
                # query.apellidos=jsonRequest['apellidos']
                # query.nombresCompleto=jsonRequest['nombresCompleto']
                # query.fechaAprobado=jsonRequest['fechaAprobado']
                # query.numeroIdentificacion=jsonRequest['numeroIdentificacion']
                # query.codigoCliente=jsonRequest['codigoCliente']
                # query.codigoCorp=jsonRequest['codigoCorp']
                # query.numeroFactura=jsonRequest['numeroFactura']
                # query.montoVenta=jsonRequest['montoVenta']
                # query.checkPagare=jsonRequest['checkPagare']
                # query.checkTablaAmortizacion=jsonRequest['checkTablaAmortizacion']
                # query.checkManualPago=jsonRequest['checkManualPago']
                # query.checkCedula=jsonRequest['checkCedula']
                # query.external_id=jsonRequest['external_id']
                # query.created_at=jsonRequest['created_at']
                # query.updated_at=jsonRequest['updated_at']
                # query.state=jsonRequest['state']
                # query.save()
            
            # Borramos SQS
            message.delete()
    except Exception as e:
        err={"error":'Un error ha ocurrido: {}'.format(e)}
        createLog(logModel,err,logExcepcion)
        print(err)
        return err



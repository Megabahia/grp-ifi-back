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
        aws_access_key_id = config.AWS_ACCESS_KEY_ID
        aws_secret_access_key = config.AWS_SECRET_ACCESS_KEY
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
            if query is None:
                serializer = CreditoPersonasSerializer(data=jsonRequest)
            else:
                serializer = CreditoPersonasSerializer(query, data=jsonRequest, partial=True)
            
            if serializer.is_valid():
                # Guardamos
                serializer.save()
                # Borramos SQS
                message.delete()
    except Exception as e:
        err={"error":'Un error ha ocurrido: {}'.format(e)}
        createLog(logModel,err,logExcepcion)
        return err



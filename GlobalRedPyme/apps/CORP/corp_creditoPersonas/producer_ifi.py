import boto3
import json

from .s3 import replicate
# Importar configuraciones
from ...config import config
import environ


def publish(data):
    topicArn = config.AWS_TOPIC_ARN
    snsClient = boto3.client(
        'sns',
        aws_access_key_id=config.AWS_ACCESS_KEY_ID_COLAS,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY_COLAS,
        region_name=config.AWS_REGION_NAME,
    )

    campos_a_eliminar = [
        'reporteBuro', 'identificacion', 'papeletaVotacion', 'identificacionConyuge',
        'papeletaVotacionConyuge', 'planillaLuzNegocio', 'planillaLuzDomicilio', 'facturas',
        'matriculaVehiculo', 'impuestoPredial', 'buroCredito', 'evaluacionCrediticia',
        'ruc', 'rolesPago', 'panillaIESS', 'mecanizadoIess', 'fotoCarnet',
        'solicitudCredito', 'buroCreditoIfis', 'documentoAprobacion', 'pagare',
        'contratosCuenta', 'tablaAmortizacion'
    ]

    for campo in campos_a_eliminar:
        if campo in data:
            data.pop(campo)
    if 'external_id' in data:
        if data['external_id'] is None:
            data['external_id'] = data['_id']
    if 'autorizacion' in data:
        autorizacion = data.pop('autorizacion')
        env = environ.Env()
        environ.Env.read_env()  # LEE ARCHIVO .ENV
        autorizacion = str(autorizacion).replace(env.str('URL_BUCKET'), '')
        if autorizacion != 'None':
            data['autorizacion'] = autorizacion
            replicate(autorizacion)

    response = snsClient.publish(
        TopicArn=topicArn,
        Message=json.dumps(data),
        Subject='PURCHASE',
    )
    print(response['ResponseMetadata']['HTTPStatusCode'])

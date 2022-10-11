import boto3
import json
# Importar configuraciones
from apps.config import config


def publish(data):
    topicArn = config.AWS_TOPIC_ARN
    snsClient = boto3.client(
        'sns',
        aws_access_key_id=config.AWS_ACCESS_KEY_ID_COLAS,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY_COLAS,
        region_name=config.AWS_REGION_NAME,
    )

    data.pop('reporteBuro')
    data.pop('identificacion')
    data.pop('papeletaVotacion')
    data.pop('identificacionConyuge')
    data.pop('papeletaVotacionConyuge')
    data.pop('planillaLuzNegocio')
    data.pop('planillaLuzDomicilio')
    data.pop('facturas')
    data.pop('matriculaVehiculo')
    data.pop('impuestoPredial')
    data.pop('buroCredito')
    data.pop('evaluacionCrediticia')
    data.pop('ruc')
    data.pop('rolesPago')
    data.pop('panillaIESS')
    data.pop('mecanizadoIess')
    data.pop('fotoCarnet')
    data.pop('solicitudCredito')
    data.pop('buroCreditoIfis')
    data.pop('documentoAprobacion')
    data.pop('pagare')
    data.pop('contratosCuenta')
    data.pop('tablaAmortizacion')

    response = snsClient.publish(
        TopicArn=topicArn,
        Message=json.dumps(data),
        Subject='PURCHASE',
        MessageAttributes={"TransactionType":{"DataType":"String","StringValue":"PURCHASE"}}
    )
    print(response['ResponseMetadata']['HTTPStatusCode'])
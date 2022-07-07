
import boto3
import json
# Importar configuraciones
from apps.config import config

def get_queue_url():
    region_name = config.AWS_REGION_NAME
    queue_name = config.AWS_QUEUE_NAME
    max_queue_messages = 10
    message_bodies = []
    aws_access_key_id=config.AWS_ACCESS_KEY_ID
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY
    sqs = boto3.resource('sqs', region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key)
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    while True:
        messages_to_delete = []
        for message in queue.receive_messages(MaxNumberOfMessages=max_queue_messages):
            # process message body
            body = json.loads(message.body)
            print(body['Message'])
            print("----------------------------------------------------------------")
            message_bodies.append(body)
            # add message to delete
            messages_to_delete.append({
                'Id': message.message_id,
                'ReceiptHandle': message.receipt_handle
            })

        # if you don't receive any notifications the
        # messages_to_delete list will be empty
        if len(messages_to_delete) == 0:
            break
        # delete messages to remove them from SQS queue
        # handle any errors
        else:
            delete_response = queue.delete_messages(
                    Entries=messages_to_delete)


    
import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['REQUEST_COUNT_TABLE_NAME'])
_lambda = boto3.client('lambda')

def handler(event, context):
    print(f'request: {json.dumps(event)}')
    method = event.get('httpMethod')
    if method == 'POST':
        table.update_item(
            Key={'path': event['path']},
            UpdateExpression='ADD request_count :incr',
            ExpressionAttributeValues={':incr': 1}
        )
    elif method == 'DELETE':
        table.update_item(
            Key={'path': event['path']},
            UpdateExpression='ADD request_count :incr',
            ExpressionAttributeValues={':incr': -1}
        )
    elif method == 'GET':
        pass
    elif method == 'PUT':
        return {
            'statusCode':401
        }
    else:
        return {
            'statusCode':501
        }
    response = _lambda.invoke(
        FunctionName = os.environ['DOWNSTREAM_FUNCTION_NAME'],
        Payload=json.dumps(event),
    )
    body = response['Payload'].read()
    print('downstream response: {}'.format(body))
    return json.loads(body)
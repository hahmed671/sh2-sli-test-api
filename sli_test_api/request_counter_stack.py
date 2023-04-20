from constructs import Construct
from aws_cdk import (
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb
)

class RequestCounter(Construct):

    @property
    def handler(self):
        return self._handler
    
    def __init__(self, scope: Construct, id: str, downstream: _lambda.IFunction, **kwargs):
        super().__init__(scope, id, **kwargs)

        table = dynamodb.Table(
            self, 'RequestCounter',
            partition_key = {'name':'path','type': dynamodb.AttributeType.STRING}
        )
        self._handler = _lambda.Function(
            self, 'RequestCounterHandler',
            runtime = _lambda.Runtime.PYTHON_3_7,
            handler='request_count.handler',
            code = _lambda.Code.from_asset('lambda'),
            environment = {
                'DOWNSTREAM_FUNCTION_NAME': downstream.function_name,
                'REQUEST_COUNT_TABLE_NAME': table.table_name
            }
        )
        table.grant_read_write_data(self._handler)
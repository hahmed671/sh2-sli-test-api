from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from .request_counter_stack import RequestCounter
from .observability_stack import ObservabilityStack

class SliTestApiStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        sli_lambda = _lambda.Function(
            self,'sli-test-lambda-handler',
            runtime = _lambda.Runtime.PYTHON_3_7,
            code = _lambda.Code.from_asset('lambda'),
            handler = 'lambda_handler.handler',
        )

        request_counter = RequestCounter(self, 'RequestCounter',downstream = sli_lambda)

        sli_lambda.grant_invoke(request_counter.handler)

        endpoint = apigw.LambdaRestApi(
            self, 'Endpoint',
            handler = request_counter._handler,
        )
        observability = ObservabilityStack(self, id='SLI-Test-API-Dashboard',api=endpoint.rest_api_name)


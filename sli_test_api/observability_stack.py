from constructs import Construct
from aws_cdk import (
    aws_cloudwatch as cw,
    Duration
)

class ObservabilityStack(Construct):
    api_gateway_metrics = {
        'Count':'Sum All Requests',
        '4XXError':'Sum 4XX Errors',
        '5XXError':'Sum 5XX Errors',
        'Latency':'Latency',
        'IntegrationLatency':'Integration Latency',
        'CacheHitCount':'Cache Hit Count',
        'CacheMissCount': 'Cache Miss Count',
    }
    def __init__(self, scope: Construct, id: str, api, **kwargs):
        super().__init__(scope, id,**kwargs)

        dashboard = cw.Dashboard(self,id,
            dashboard_name = id,
        )
        for key in self.api_gateway_metrics:
            dashboard.add_widgets(
                cw.GraphWidget(
                    title = f'{id.replace("-"," ")} {self.api_gateway_metrics[key]}',
                    width=12,
                    left=[
                        cw.Metric(
                            namespace='AWS/ApiGateway',
                            metric_name=key,
                            dimensions_map={
                                'ApiName':api
                            },
                            statistic='sum',
                            label=self.api_gateway_metrics[key],
                            period=Duration.minutes(1)
                        )
                    ]
                )
        )

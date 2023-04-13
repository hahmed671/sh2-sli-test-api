import aws_cdk as core
import aws_cdk.assertions as assertions
from sli_test_api.sli_test_api_stack import SliTestApiStack


def test_sqs_queue_created():
    app = core.App()
    stack = SliTestApiStack(app, "sli-test-api")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = SliTestApiStack(app, "sli-test-api")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)

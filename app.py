#!/usr/bin/env python3

import aws_cdk as cdk

from sli_test_api.sli_test_api_stack import SliTestApiStack


app = cdk.App()
SliTestApiStack(app, "sli-test-api")

app.synth()

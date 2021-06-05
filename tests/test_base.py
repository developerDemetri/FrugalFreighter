from os import environ
from unittest import TestCase
from unittest.mock import patch

from frugal_freighter.type_defs import EventBridgeEvent


# pylint: disable=line-too-long
class TestBase(TestCase):
    """
    Base Class for unit testing
    """

    mock_interruption_event: EventBridgeEvent = {
        "version": "0",
        "id": "9bcdac79-b31f-4d3d-9410-fbd727c29fab",
        "detail-type": "ECS Task State Change",
        "source": "aws.ecs",
        "account": "111122223333",
        "time": "2019-11-19T19:55:38Z",
        "region": "us-east-1",
        "resources": [
            "arn:aws:ecs:us-east-1:111122223333:task/b99d40b3-5176-4f71-9a52-9dbd6f1cebef"
        ],
        "detail": {
            "clusterArn": "arn:aws:ecs:us-east-1:111122223333:cluster/default",
            "createdAt": "2016-12-06T16:41:05.702Z",
            "desiredStatus": "STOPPED",
            "lastStatus": "RUNNING",
            "stoppedReason": "Your Spot Task was interrupted.",
            "stopCode": "TerminationNotice",
            "taskArn": "arn:aws:ecs:us-east-1:111122223333:task/b99d40b3-5176-4f71-9a52-9dbd6fEXAMPLE",
        },
    }

    mock_placement_event: EventBridgeEvent = {
        "version": "0",
        "id": "ddca6449-b258-46c0-8653-e0e3a6d0468b",
        "detail-type": "ECS Service Action",
        "source": "aws.ecs",
        "account": "111122223333",
        "time": "2019-11-19T19:55:38Z",
        "region": "us-west-2",
        "resources": ["arn:aws:ecs:us-west-2:111122223333:service/default/servicetest"],
        "detail": {
            "eventType": "ERROR",
            "eventName": "SERVICE_TASK_PLACEMENT_FAILURE",
            "clusterArn": "arn:aws:ecs:us-west-2:111122223333:cluster/default",
            "capacityProviderArns": [
                "arn:aws:ecs:us-west-2:111122223333:capacity-provider/FARGATE_SPOT"
            ],
            "reason": "RESOURCE:FARGATE",
            "createdAt": "2019-11-06T19:09:33.087Z",
        },
    }

    @classmethod
    def setUpClass(cls) -> None:
        """
        Ensure AWS sessions are mocked out before starting tests
        """

        environ["AWS_ACCESS_KEY_ID"] = "mock"
        environ["AWS_SECRET_ACCESS_KEY"] = "mock"

    def tearDown(self) -> None:
        """
        Ensure flexmock is cleared out after each test
        """

        patch.stopall()
        return super().tearDown()

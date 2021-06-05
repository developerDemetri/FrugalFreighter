from typing import List, TypedDict, Union


class EcsEventDetail(TypedDict):
    """
    Details around ECS events
    """

    clusterArn: str
    createdAt: str


class InterruptionDetail(EcsEventDetail):
    """
    Details around ECS Fargate Spot interruption
    """

    desiredStatus: str
    lastStatus: str
    stoppedReason: str
    stopCode: str
    taskArn: str


class PlacementFailureDetail(EcsEventDetail):
    """
    Details around ECS Fargate Task Placement Failure
    """

    eventType: str
    eventName: str
    capacityProviderArns: List[str]
    reason: str


# https://aws.amazon.com/blogs/compute/deep-dive-into-fargate-spot-to-run-your-ecs-tasks-for-up-to-70-less/
# https://www.python.org/dev/peps/pep-0589/#alternative-syntax due to detail-type
EventBridgeEvent = TypedDict(
    "EventBridgeEvent",
    {
        "version": str,
        "id": str,
        "detail-type": str,
        "source": str,
        "account": str,
        "time": str,
        "region": str,
        "resources": List[str],
        "detail": Union[InterruptionDetail, PlacementFailureDetail],
    },
)

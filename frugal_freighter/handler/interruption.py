from logging import getLogger

from frugal_freighter.type_defs import EventBridgeEvent
from frugal_freighter.handler.event import EventHandler

LOGGER = getLogger("FrugalFreighter")


class SpotInterruptionHandler(EventHandler):
    """
    Handles Fargate termination notices
    """

    def __init__(self, event: EventBridgeEvent) -> None:
        pass

    def handle(self) -> None:
        pass

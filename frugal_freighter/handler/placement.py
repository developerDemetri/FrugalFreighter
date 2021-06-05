from logging import getLogger

from frugal_freighter.handler.event import EventHandler

LOGGER = getLogger("FrugalFreighter")


class PlacementFailureHandler(EventHandler):
    """
    Handles Fargate Service Task Placement Failure
    """

    def handle(self) -> None:
        pass

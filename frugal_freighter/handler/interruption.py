from logging import getLogger

from frugal_freighter.handler.event import EventHandler

LOGGER = getLogger("FrugalFreighter")


class SpotInterruptionHandler(EventHandler):
    """
    Handles Fargate termination notices
    """

    def handle(self) -> None:
        """
        Handle Spot Termination
        """

        raise NotImplementedError()

from logging import getLogger

from frugal_freighter.handler.event import EventHandler
from frugal_freighter.handler.interruption import SpotInterruptionHandler
from frugal_freighter.handler.placement import PlacementFailureHandler
from frugal_freighter.type_defs import EventBridgeEvent

LOGGER = getLogger("FrugalFreighter")


class EventHandlerFactory:
    """
    Handles EventHandler assembly
    """

    @staticmethod
    def get_handler(event: EventBridgeEvent) -> EventHandler:
        """
        Returns correct EventHandler for given event
        """

        LOGGER.info("Assembling EventHandler...")
        event_handler: EventHandler
        event_type = event.get("detail-type")
        LOGGER.debug(f"Assembling handler for event type: {event_type}")
        if event_type == "ECS Task State Change":
            LOGGER.info("Assembling SpotInterruptionHandler...")
            event_handler = SpotInterruptionHandler(event)
            LOGGER.info("Assembled SpotInterruptionHandler.")
            return event_handler

        if event_type == "ECS Service Action":
            LOGGER.info("Assembling PlacementFailureHandler...")
            event_handler = PlacementFailureHandler(event)
            LOGGER.info("Assembled PlacementFailureHandler.")
            return event_handler

        err_msg = f"Invalid event type: {event_type}"
        LOGGER.error(f"Failed to assemble EventHandler: {err_msg}")
        raise ValueError(err_msg)

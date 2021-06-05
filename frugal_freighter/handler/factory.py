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
        LOGGER.debug(f"Assembling handler for event type: {event}")

        if EventHandlerFactory.is_spot_interruption(event):
            LOGGER.info("Assembling SpotInterruptionHandler...")
            event_handler = SpotInterruptionHandler(event)
            LOGGER.info("Assembled SpotInterruptionHandler.")
            return event_handler

        if EventHandlerFactory.is_placement_failure(event):
            LOGGER.info("Assembling PlacementFailureHandler...")
            event_handler = PlacementFailureHandler(event)
            LOGGER.info("Assembled PlacementFailureHandler.")
            return event_handler

        err_msg = f"Invalid event type: {event}"
        LOGGER.error(f"Failed to assemble EventHandler: {err_msg}")
        raise ValueError(err_msg)

    @staticmethod
    def is_spot_interruption(event: EventBridgeEvent) -> bool:
        """
        Determine if event is a Spot Interruption
        """

        LOGGER.info("Checking if event is Spot Interruption...")
        is_state_change = event.get("detail-type") == "ECS Task State Change"
        LOGGER.debug(f"Event is State Change: {is_state_change}")
        is_stop_desired = event.get("detail", {}).get("desiredStatus") == "STOPPED"
        LOGGER.debug(f"Event Desires Stopped State: {is_stop_desired}")
        is_notice = event.get("detail", {}).get("stopCode") == "TerminationNotice"
        LOGGER.debug(f"Event is Termination Notice: {is_notice}")

        is_interruption = all(
            [
                is_state_change,
                is_stop_desired,
                is_notice,
            ]
        )
        LOGGER.info(f"Event is Spot Interruption: {is_interruption}")
        return is_interruption

    @staticmethod
    def is_placement_failure(event: EventBridgeEvent) -> bool:
        """
        Determine if event is a Spot Placement Failure
        """

        LOGGER.info("Checking if event is Spot Placement Failure...")
        is_service_action = event.get("detail-type") == "ECS Service Action"
        LOGGER.debug(f"Event is Service Action: {is_service_action}")
        is_error = event.get("detail", {}).get("eventType") == "ERROR"
        LOGGER.debug(f"Event is Error: {is_error}")
        is_failure_event = (
            event.get("detail", {}).get("eventName") == "SERVICE_TASK_PLACEMENT_FAILURE"
        )
        LOGGER.debug(f"Event is Failure: {is_failure_event}")

        is_failure = all(
            [
                is_service_action,
                is_error,
                is_failure_event,
            ]
        )
        LOGGER.info(f"Event is Spot Placement Failure: {is_failure}")
        return is_failure

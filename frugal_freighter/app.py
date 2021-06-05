from logging import DEBUG, INFO, getLogger, StreamHandler
from os import environ
from typing import Any

from ecs_logging import StdlibFormatter

from frugal_freighter.type_defs import EventBridgeEvent
from frugal_freighter.handler.factory import EventHandlerFactory

DEBUGGING = environ.get("DEBUGGING", "false").lower() == "true"
LOGGER = getLogger("FrugalFreighter")
ecs_handler = StreamHandler()
ecs_handler.setFormatter(StdlibFormatter())
LOGGER.addHandler(ecs_handler)
LOGGER.setLevel(DEBUG if DEBUGGING else INFO)


def lambda_handler(event: EventBridgeEvent, _: Any) -> None:
    """
    Lambda entrypoint
    """

    LOGGER.info("Handling event from EventBridge...")
    LOGGER.debug(f"EventBridge event: {event}")
    event_source = event.get("source")
    if event_source != "aws.ecs":
        err_msg = f"Invalid event source: {event_source}"
        LOGGER.error(err_msg)
        raise ValueError(err_msg)

    event_handler = EventHandlerFactory.get_handler(event)
    event_handler.handle()
    LOGGER.info("Successfully handled event from EventBridge.")

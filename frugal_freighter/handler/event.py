from abc import ABC, abstractmethod

from frugal_freighter.type_defs import EventBridgeEvent


class EventHandler(ABC):
    """
    Handles ECS Fargate Events
    """

    def __init__(self, event: EventBridgeEvent) -> None:
        pass

    @abstractmethod
    def handle(self) -> None:
        """
        Process event
        """

        raise NotImplementedError()

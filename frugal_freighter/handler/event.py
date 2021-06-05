from abc import ABC, abstractmethod


class EventHandler(ABC):
    """
    Handles ECS Fargate Events
    """

    @abstractmethod
    def handle(self) -> None:
        """
        Process event
        """

        raise NotImplementedError()

from abc import ABC, abstractmethod


class LoadBalancer(ABC):
    """
    Orchestrates load balancers
    """

    @abstractmethod
    def deregister(self) -> None:
        """
        Safely deregister load balancer
        """

        raise NotImplementedError()

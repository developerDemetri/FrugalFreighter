from logging import getLogger

from frugal_freighter.loadbalancing.elb import LoadBalancer

LOGGER = getLogger("FrugalFreighter")


class ApplicationLB(LoadBalancer):
    """
    Handles ALB orchestration
    """

    def __init__(self) -> None:
        pass

    def deregister(self) -> None:
        pass

from logging import getLogger

from frugal_freighter.loadbalancing.elb import LoadBalancer

LOGGER = getLogger("FrugalFreighter")


class NetworkLB(LoadBalancer):
    """
    Handles NLB orchestration
    """

    def deregister(self) -> None:
        pass

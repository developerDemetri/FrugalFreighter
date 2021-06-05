from logging import getLogger

from frugal_freighter.loadbalancing.elb import LoadBalancer

LOGGER = getLogger("FrugalFreighter")


class ApplicationLB(LoadBalancer):
    """
    Handles ALB orchestration
    """

    def deregister(self) -> None:
        """
        Deregister ALB target
        """

        raise NotImplementedError()

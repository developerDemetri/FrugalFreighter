from logging import getLogger

from frugal_freighter.loadbalancing.alb import ApplicationLB
from frugal_freighter.loadbalancing.elb import LoadBalancer
from frugal_freighter.loadbalancing.nlb import NetworkLB

LOGGER = getLogger("FrugalFreighter")


class LoadBalancerFactory:
    """
    Handles LoadBalancer assembly
    """

    @staticmethod
    def get_load_balancer(lb_type: str) -> LoadBalancer:
        """
        Returns specified load balancer orchestrator
        """

        LOGGER.debug(f"Assembling LoadBalancer of type {lb_type}...")
        loadbalancer: LoadBalancer
        if lb_type == "ALB":
            LOGGER.info("Assembling ApplicationLB...")
            loadbalancer = ApplicationLB()
            LOGGER.info("Assembled ApplicationLB.")
            return loadbalancer

        if lb_type == "NLB":
            LOGGER.info("Assembling NetworkLB...")
            loadbalancer = NetworkLB()
            LOGGER.info("Assembled NetworkLB.")
            return loadbalancer

        err_msg = f"Invalid load balancer type: {lb_type}"
        LOGGER.error(f"Failed to assemble LoadBalancer: {err_msg}")
        raise ValueError(err_msg)

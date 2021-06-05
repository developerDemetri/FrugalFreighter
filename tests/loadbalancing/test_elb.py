from unittest.mock import patch

from tests.test_base import TestBase

from frugal_freighter.loadbalancing.elb import LoadBalancer


# pylint: disable=abstract-class-instantiated
class TestLoadBalancer(TestBase):
    """
    Test the LoadBalancer base class
    """

    def setUp(self) -> None:
        """
        Setup mocks
        """

        super().setUp()
        patch.object(LoadBalancer, "__abstractmethods__", set()).start()

    def test_not_implemented(self):
        """
        Verify no direct usage of base class
        """

        test_lb = LoadBalancer()

        with self.assertRaises(NotImplementedError):
            test_lb.deregister()

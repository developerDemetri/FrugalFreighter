from unittest.mock import patch, Mock

from tests.test_base import TestBase

from frugal_freighter.loadbalancing.factory import LoadBalancerFactory


class TestLoadBalancerFactory(TestBase):
    """
    Test creation of LoadBalancers
    """

    def test_with_alb(self):
        """
        Verify ApplicationLB creation
        """

        mock_lb = Mock()
        mock_alb = patch("frugal_freighter.loadbalancing.factory.ApplicationLB").start()
        mock_alb.return_value = mock_lb

        load_balancer = LoadBalancerFactory.get_load_balancer("ALB")

        mock_alb.assert_called_once_with()
        self.assertEqual(mock_lb, load_balancer)

    def test_with_nlb(self):
        """
        Verify NetworkLB creation
        """

        mock_lb = Mock()
        mock_nlb = patch("frugal_freighter.loadbalancing.factory.NetworkLB").start()
        mock_nlb.return_value = mock_lb

        load_balancer = LoadBalancerFactory.get_load_balancer("NLB")

        mock_nlb.assert_called_once_with()
        self.assertEqual(mock_lb, load_balancer)

    def test_with_bad_type(self):
        """
        Should throw error on invalid type
        """

        bad_type = "ELB"

        with self.assertRaises(ValueError):
            LoadBalancerFactory.get_load_balancer(bad_type)

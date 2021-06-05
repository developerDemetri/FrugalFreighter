from copy import deepcopy
from unittest.mock import patch, Mock

from tests.test_base import TestBase

from frugal_freighter.handler.factory import EventHandlerFactory


class TestEventHandlerFactory(TestBase):
    """
    Test creation of EventHandlers
    """

    def test_with_interruption(self):
        """
        Verify SpotInterruptionHandler creation
        """

        mock_handler = Mock()
        mock_interruption = patch(
            "frugal_freighter.handler.factory.SpotInterruptionHandler"
        ).start()
        mock_interruption.return_value = mock_handler

        handler = EventHandlerFactory.get_handler(self.mock_interruption_event)

        mock_interruption.assert_called_once_with(self.mock_interruption_event)
        self.assertEqual(mock_handler, handler)

    def test_with_placement_failure(self):
        """
        Verify PlacementFailureHandler creation
        """

        mock_handler = Mock()
        mock_placement = patch(
            "frugal_freighter.handler.factory.PlacementFailureHandler"
        ).start()
        mock_placement.return_value = mock_handler

        handler = EventHandlerFactory.get_handler(self.mock_placement_event)

        mock_placement.assert_called_once_with(self.mock_placement_event)
        self.assertEqual(mock_handler, handler)

    def test_with_bad_event(self):
        """
        Should throw error on invalid event
        """

        bad_event = deepcopy(self.mock_interruption_event)
        bad_event["detail-type"] = "ECS Task Deleted"

        with self.assertRaises(ValueError):
            EventHandlerFactory.get_handler(bad_event)

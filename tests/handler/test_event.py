from unittest.mock import patch

from tests.test_base import TestBase

from frugal_freighter.handler.event import EventHandler


# pylint: disable=abstract-class-instantiated
class TestEventHandler(TestBase):
    """
    Test the EventHandler base class
    """

    def setUp(self) -> None:
        """
        Setup mocks
        """

        super().setUp()
        patch.object(EventHandler, "__abstractmethods__", set()).start()

    def test_not_implemented(self):
        """
        Verify no direct usage of base class
        """

        test_handler = EventHandler(self.mock_interruption_event)

        with self.assertRaises(NotImplementedError):
            test_handler.handle()

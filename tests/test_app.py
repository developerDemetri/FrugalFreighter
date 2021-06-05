from copy import deepcopy
from unittest.mock import patch, Mock

from frugal_freighter import app

from tests.test_base import TestBase


class TestApp(TestBase):
    """
    Test Application entrypoint
    """

    def setUp(self) -> None:
        """
        Setup mocks
        """

        super().setUp()
        self.mock_handler = Mock()
        self.mock_factory = patch("frugal_freighter.app.EventHandlerFactory").start()
        self.mock_factory.get_handler.return_value = self.mock_handler


class TestLambdaHandler(TestApp):
    """
    Test Lambda entrypoint
    """

    def test_get_handler_call(self) -> None:
        """
        Verify get_handler call
        """

        app.lambda_handler(self.mock_interruption_event, None)

        self.mock_factory.get_handler.assert_called_once_with(
            self.mock_interruption_event
        )

    def test_handle_call(self) -> None:
        """
        Verify handle call
        """

        app.lambda_handler(self.mock_interruption_event, None)

        self.mock_handler.handle.assert_called_once_with()

    def test_bad_event_source(self) -> None:
        """
        Should throw error if bad event source
        """

        bad_event = deepcopy(self.mock_interruption_event)
        bad_event["source"] = "aws.lambda"

        with self.assertRaises(ValueError):
            app.lambda_handler(bad_event, None)

        self.mock_factory.get_handler.assert_not_called()

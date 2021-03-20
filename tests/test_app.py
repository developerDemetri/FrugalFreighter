from frugal_freighter import app

from tests.test_base import TestBase


class TestApp(TestBase):
    """
    Test Application entrypoint
    """

    def test_handler(self) -> None:
        """
        Test Handler happy path
        """
        resp = app.handler(self.mock_event, None)
        self.assertEqual("TODO", resp)

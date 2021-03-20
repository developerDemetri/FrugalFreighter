from os import environ
from typing import Any, Dict
from unittest import TestCase

from flexmock import flexmock_teardown


class TestBase(TestCase):
    """
    Base Class for unit testing
    """

    mock_event: Dict[str, Any] = dict()

    @classmethod
    def setUpClass(cls) -> None:
        """
        Ensure AWS sessions are mocked out before starting tests
        """
        environ["AWS_ACCESS_KEY_ID"] = "mock"
        environ["AWS_SECRET_ACCESS_KEY"] = "mock"

    def tearDown(self) -> None:
        """
        Ensure flexmock is cleared out after each test
        """
        flexmock_teardown()
        return super().tearDown()

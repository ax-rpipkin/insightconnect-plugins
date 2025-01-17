import sys
import os
from unittest import TestCase
from unittest.mock import patch
from icon_cybereason.actions.isolate_machine import IsolateMachine
from icon_cybereason.actions.isolate_machine.schema import Input, Output
from unit_test.util import Util

sys.path.append(os.path.abspath("../"))


class TestIsolateMachine(TestCase):
    @classmethod
    @patch("requests.sessions.Session.post", side_effect=Util.mocked_requests_session)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(IsolateMachine())

    @patch("requests.sessions.Session.request", side_effect=Util.mocked_requests_session)
    def test_isolate_machine(self, mock_request):
        actual = self.action.run(
            {
                Input.SENSOR: "desktop-sb01",
                Input.QUARANTINE_STATE: True,
                Input.MALOP_ID: "11.-7592746539469363637",
            }
        )
        expected = {"machine_id": "machine_pylum_id", "success": True}
        self.assertEqual(actual, expected)

    @patch("requests.sessions.Session.request", side_effect=Util.mocked_requests_session)
    def test_unisolate_machine(self, mock_request):
        actual = self.action.run(
            {
                Input.SENSOR: "desktop-sb01",
                Input.QUARANTINE_STATE: False,
                Input.MALOP_ID: "11.-7592746539469363637",
            }
        )
        expected = {"machine_id": "machine_pylum_id", "success": True}
        self.assertEqual(actual, expected)

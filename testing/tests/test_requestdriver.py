from requestdriver import RequestDriver
from testing.stubs import SessionStub
from unittest2 import TestCase


class TestRequestDriver(TestCase):

    def setUp(self):

        class data(object):
            requestdriver = RequestDriver()

        self.data = data()

    def test_method_request(self):
        """Test arguments are correctly passed to the session request method"""

        # Kwargs directly passed to request call
        kwargs = {
            'uri': 0,
            'method': self.data.requestdriver.GET,
            'headers': 1,
            'params': 2,
            'data': 3,
            'files': 4,
            'cookies': 5
        }

        session_stub = SessionStub()

        self.data.requestdriver.session = session_stub
        response = self.data.requestdriver.request(**kwargs)

        # Kwargs not passed to request call
        kwargs.update({
            'verify': self.data.requestdriver.verify_certificates
        })
        session_stub.request.assert_called_once_with(**kwargs)

    def test_method_get_last_response_with_responses(self):
        """Tests that trying to access the last response returns the last response"""
        responses = []
        for i in xrange(0, 10):
            responses.append(i)

        self.data.requestdriver.responses = responses
        last_response = self.data.requestdriver.get_last_response()

        self.assertEqual(i, last_response)

    def test_method_get_last_response_with_no_responses(self):
        """Tests that trying to access the last response with no responses returns None (not error)"""
        self.data.requestdriver.responses = []
        last_response = self.data.requestdriver.get_last_response()

        self.assertIs(None, last_response)

    def test_method_wipe_session(self):
        """Tests that the session is no longer the old session"""
        old_session = 'old session'
        self.data.requestdriver.session = old_session
        self.data.requestdriver.wipe_session()

        new_session = self.data.requestdriver.session
        self.assertNotEqual(old_session, new_session)

    def test_method_save_last_response_to_file(self):
        """"""

    def test_method_save_response_to_file(self):
        """"""
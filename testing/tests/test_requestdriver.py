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

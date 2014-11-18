from unittest import TestCase

import mock
from requestdriver import RequestDriver

from testing.stubs import SessionStub, ResponseStub


class TestRequestDriver(TestCase):
    """Tests for RequestDriver methods"""

    def setUp(self):
        """Setup the data for each test method"""

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
        """Tests that the save to file is called with last response"""
        response = 100
        filename = 99

        self.data.requestdriver.get_last_response = mock.Mock(return_value=response)
        self.data.requestdriver.save_response_to_file = mock.Mock()

        self.data.requestdriver.save_last_response_to_file(filename)
        self.data.requestdriver.save_response_to_file.assert_called_with(response, filename)

    def test_method_save_response_to_file(self):
        """Tests that we write to the correct file and with the correct content for a given response"""
        test_content = 'stubbed response content'
        fake_filename = 'fakefile'

        m = mock.mock_open()
        with mock.patch('__builtin__.open', m) as mock_open:
            response = ResponseStub()
            response.content = test_content

            self.data.requestdriver.save_response_to_file(response, fake_filename)

            # Test the correct filename was opened
            mock_open.assert_called_once_with(fake_filename, 'w')

            # Test that the file was written to with correct content
            file_handle = mock_open.return_value.__enter__.return_value
            file_handle.write.assert_called_with(test_content)
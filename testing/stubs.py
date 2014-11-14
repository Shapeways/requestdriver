from mock import Mock


class ResponseStub(object):
    """Stub for Response object in requests"""


class SessionStub(object):
    """Stub for the Session object in requests"""

    request = Mock(return_value=ResponseStub())
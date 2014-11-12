from mock import Mock


class ResponseStub(object):

    pass


class SessionStub(object):

    request = Mock(return_value=ResponseStub())
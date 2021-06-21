class InternalServerError(Exception):
    def __init__(self, message: str = 'oopsie looks like something on our server broke again'):
        super(InternalServerError, self).__init__(message)


class ConError(Exception):
    def __init__(self,
                 message: str = ":O unable to connect to the servers"):
        super(ConError, self).__init__(message)


class BadGateway(Exception):
    def __init__(self,
                 message: str = 'ERR: 502 Bad Gateway Error'):
        super(BadGateway, self).__init__(message)


class PageNotFound(Exception):
    def __init__(self, message: str = "Page Not Found 404"):
        super(PageNotFound, self).__init__(message)


class RateLimitted(Exception):
    def __init__(self, message: str = "Please Try Again after sometime you are being ratelimitted"):
        super(RateLimitted, self).__init__(message)

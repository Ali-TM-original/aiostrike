from .exceptions import *


class ExceptionCheck:
    def __init__(self, status_code: int):
        self.status_code = status_code

    def check(self):
        if self.status_code >= 200:
            pass
        elif self.status_code >= 500:
            if self.status_code == 502:
                raise BadGateway()
            raise InternalServerError()
        elif self.status_code >= 400:
            raise PageNotFound()

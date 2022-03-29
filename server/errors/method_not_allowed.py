from server.errors import APIError
from http import HTTPStatus


class MethodNotAllowedError(APIError):
    def __init__(self, message):
        super().__init__(message, status_code=HTTPStatus.METHOD_NOT_ALLOWED)

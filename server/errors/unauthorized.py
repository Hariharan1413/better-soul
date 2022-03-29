from server.errors.api_error import APIError
from http import HTTPStatus


class UnauthorizedError(APIError):
    def __init__(self, message):
        super().__init__(message, HTTPStatus.UNAUTHORIZED)

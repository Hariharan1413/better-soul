from http import HTTPStatus
from server.errors.api_error import APIError


class ForbiddenError(APIError):
    def __init__(self, message):
        super().__init__(message, status_code=HTTPStatus.FORBIDDEN)

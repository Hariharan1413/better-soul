from http import HTTPStatus


class APIError(Exception):
    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        if status_code:
            self.status_code = status_code
        self.message = message
        self.payload = payload

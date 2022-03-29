import os
from flask import Blueprint, jsonify, current_app
from server.config import DevelopmentConfig
from server.errors.api_error import APIError
from server.errors.no_content import NoContentError
from http import HTTPStatus

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(Exception)
def error_handler(e):
    err = {
        "status_code": HTTPStatus.INTERNAL_SERVER_ERROR,
        "message": "Something went wrong, please try again later.",
    }

    if isinstance(e, APIError):
        err["status_code"] = e.status_code
        err["message"] = e.message
    elif e.__class__.__name__ == "NotFound":
        err["status_code"] = HTTPStatus.NOT_FOUND
        err["message"] = "Route not found."
    else:
        if os.environ.get("FLASK_ENV") == "development":
            err["message"] = repr(e)
    return jsonify(err), err["status_code"]

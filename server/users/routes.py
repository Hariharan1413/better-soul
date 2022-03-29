from flask import Blueprint, jsonify, request
from server import classifier
from server.errors import BadRequestError
from http import HTTPStatus
from pandas import DataFrame
from numpy import log1p
from server.auth.utils import tokens_required

user = Blueprint("user", __name__, url_prefix="/api/v1/user")


@user.route("/classifier", methods=["POST"])
@tokens_required
def classify(user_id):
    req = request.json
    if not req:
        raise BadRequestError("No data to classify.")
    features, values = [], []
    for feature, value in req.items():
        features.append("log_" + feature)
        values.append(log1p(value))
    prediction = int(classifier.predict(DataFrame([values], columns=features)))
    return (
        jsonify(
            status_code=HTTPStatus.OK,
            message="Prediction successful",
            data={"prediction": prediction},
        ),
        HTTPStatus.OK,
    )

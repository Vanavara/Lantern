# stdlib
from enum import Enum


class StatusCodeEnum(Enum):
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    UNPROCESSABLE = 422
    TOO_MANY_REQUESTS = 429
    SERVER_ERROR = 500


class ErrorResponseEnum(Enum):
    SOMETHING_WENT_WRONG = (StatusCodeEnum.SERVER_ERROR, "Something went wrong")
    INCORRECT_CREDENTIALS = (StatusCodeEnum.UNAUTHORIZED, "Incorrect credentials")
    FORBIDDEN = (StatusCodeEnum.FORBIDDEN, "Forbidden")

    def __init__(self, http_code, message):
        self.http_code = http_code
        self.detail = message

from flask import jsonify, Response
from pydantic import ValidationError
from typing import Tuple

def handle_validation_error(e: ValidationError) -> Tuple[Response, int]:
    """
    Handles validation errors thrown by Pydantic models.

    Args:
        e (ValidationError): The exception raised by Pydantic validation.

    Returns:
        Tuple[Response, int]: A Flask response object with error details and
        the HTTP status code.
    """
    details = e.errors()
    modified_details = []
    # Replace 'msg' with 'message' for each error
    for error in details:
        modified_details.append(
            {
                "loc": error["loc"],
                "message": error["msg"],
                "type": error["type"],
            }
        )
    return jsonify({"error": "Validation error", "details": modified_details}), 400


def handle_value_error(e: ValueError) -> Tuple[Response, int]:
    """
    Handles generic value errors typically related to data processing.

    Args:
        e (ValueError): The exception raised.

    Returns:
        Tuple[Response, int]: A Flask response object with error details and
        the HTTP status code.
    """
    return jsonify({"error": str(e)}), 400
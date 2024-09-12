
from flask import request, jsonify, g, Response, make_response
from app.modules.user.serialization.user_serializer import UserSerializer
from app.modules.auth.schemas.post_register_schema import PostRegisterDto
from typing import Dict, Any
import logging
from app.modules.auth import auth_bp as bp

logger = logging.getLogger(__name__)

@bp.route('/register', methods=['POST'])
def register() -> Response:
    """
    Create a new user based on the provided JSON data
    and serialize the created user.

    Returns:
        Response: A JSON response with the serialized created user and HTTP
        status code 201.
    """
    post_register_service = g.container.resolve('post_register_service')

    try:
        data = request.json
    except Exception as e:
        logger.error(f"Failed to parse JSON from request: {str(e)}")
        return make_response(jsonify({'message': 'Invalid JSON format'}), 400)

    user_dto: PostRegisterDto = UserSerializer.deserialize_create(
        data)
    created_user = post_register_service.register(user_dto)
    serialized_user: Dict[str, Any] = UserSerializer.serialize_response(created_user)
    return make_response(jsonify(serialized_user), 201)

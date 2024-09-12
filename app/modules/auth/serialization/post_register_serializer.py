
from app.libs.serialization.base_serializer import BaseSerializer
from app.modules.auth.schemas.post_register_schema import (PostRegisterDto, PostResponseResponseDto)

class PostRegisterSerializer(BaseSerializer):
    @staticmethod
    def serialize_response(user: PostResponseResponseDto) -> dict:
        """
        Serializes a PostResponseResponseDto into a dictionary.

        Args:
            user (PostResponseResponseDto): The user response data.

        Returns:
            dict: The serialized user response.
        """
        return BaseSerializer.serialize(user)

    @staticmethod
    def deserialize_create(data: dict) -> PostRegisterDto:
        """
        Deserializes a dictionary into a PostRegisterDto.

        Args:
            data (dict): The data to deserialize.

        Returns:
            PostRegisterDto: The deserialized user register data.
        """
        return BaseSerializer.deserialize(data, PostRegisterDto)
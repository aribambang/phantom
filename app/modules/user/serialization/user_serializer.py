from app.libs.serialization.base_serializer import BaseSerializer
from app.modules.user.schemas.user import (UserCreateDto, UserResponseDto)

class UserSerializer(BaseSerializer):
    @staticmethod
    def serialize_response(user: UserResponseDto) -> dict:
        """
        Serializes a UserResponseDto into a dictionary.

        Args:
            user (UserResponseDto): The user response data.

        Returns:
            dict: The serialized user response.
        """
        return BaseSerializer.serialize(user)

    @staticmethod
    def deserialize_create(data: dict) -> UserCreateDto:
        """
        Deserializes a dictionary into a UserCreateDto.

        Args:
            data (dict): The data to deserialize.

        Returns:
            UserCreateDto: The deserialized user register data.
        """
        return BaseSerializer.deserialize(data, UserCreateDto)
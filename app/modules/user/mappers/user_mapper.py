from typing import Dict, Any, List
from app.libs.mappers.base_mapper import BaseMapper
from app.modules.user.models.domain.user import User
from app.modules.user.models.database.user import UserTable
from app.modules.user.schemas.user import (
    UserCreateDto,
    UserResponseDto,
)
import logging

logger = logging.getLogger(__name__)

class UserMapper(BaseMapper[User]):
    """
    Mapper class for the User entity. Handles conversions between
    domain model, database model, and DTOs.
    """

    @classmethod
    def to_domain(cls, data: Dict[str, Any]) -> User:
        """
        Convert a dictionary to a User domain model instance.

        Args:
            data (Dict[str, Any]): The dictionary containing user data.

        Returns:
            User: An instance of the User domain model.
        """
        return User(
            id=getattr(data, 'id'),
            name=getattr(data, 'name'),
            email=getattr(data, 'email')
        )

    @classmethod
    def to_dto(cls, domain_model: User) -> UserResponseDto:
        """
        Convert a User domain model instance to a UserResponseDto.

        Args:
            domain_model (User): The User domain model instance.

        Returns:
            UserResponseDto: A DTO representing the user.
        """
        return UserResponseDto(
            id=domain_model.id,
            name=domain_model.name,
            email=domain_model.email
        )

    @classmethod
    def from_create_dto(cls, dto: UserCreateDto) -> User:
        """
        Create a User domain model instance from a UserCreateDto.

        Args:
            dto (UserCreateDto): The DTO containing data
            for creating a user.

        Returns:
            User: A new instance of the User domain model.
        """
        return User(
            id=None,  # ID will be assigned by the database
            name=dto.name,
            email=dto.email,
        )

    @classmethod
    def from_persistence(cls, db_model: UserTable) -> User:
        """
        Convert a UserTable database model to a User domain model.

        Args:
            db_model (UserTable): The database model instance.

        Returns:
            User: An instance of the User domain model.
        """
        return User(
            id=db_model.id,
            name=db_model.name,
            email=db_model.email
        )

    @classmethod
    def to_persistence_model(cls, domain_model: User) -> UserTable:
        """
        Convert a User domain model to a UserTable database model.

        Args:
            domain_model (User): The User domain model instance.

        Returns:
            UserTable: An instance of the UserTable database model.
        """
        return UserTable(
            id=domain_model.id,
            name=domain_model.name,
            email=domain_model.email,
            password=domain_model.password
        )

    @classmethod
    def map_domain_list(cls, users: List[User]) -> List[UserResponseDto]:
        """
        Map a list of User domain models to a list of UserResponseDto.

        Args:
            users (List[User]): A list of User domain models.

        Returns:
            List[UserResponseDto]: A list of UserResponseDto instances.
        """
        return [cls.to_dto(user) for user in users]
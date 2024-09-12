from typing import List, Optional
from app.modules.user.repositories.user_repository import UserRepository
from app.modules.user.models.domain.user import User
from app.modules.user.schemas.user import (
    UserCreateDto,
    UserResponseDto,
)
from app import bcrypt
import logging

logger = logging.getLogger(__name__)

class UserService:
    """Service layer for handling user-related operations."""

    def __init__(
        self,
        user_repository: UserRepository,
    ):
        """
        Initializes the UserService with required repositories.

        Args:
            user_repository (UserRepository): Repository for user data.
        """
        self.user_repository: UserRepository = user_repository

    def find_by_id(self, id: int) -> Optional[UserResponseDto]:
        """
        Finds a user by their ID and returns their data.

        Args:
            id (int): The ID of the user to find.

        Returns:
            Optional[UserResponseDto]: The user's data,
            or None if not found.
        """
        user: Optional[User] = self.user_repository.find_by_id(id)
        if user:
            return UserResponseDto(
                id=user.id,
                name=user.name,
                email=user.email
            )
        return None
    
    def find_by_email(self, email: str) -> Optional[UserResponseDto]:
        """
        Finds a user by their email and returns their data.

        Args:
            email (str): The email of the user to find.

        Returns:
            Optional[UserResponseDto]: The user's data,
            or None if not found.
        """
        user: Optional[User] = self.user_repository.find_by_email(email)
        if user:
            return UserResponseDto(
                id=user.id,
                name=user.name,
                email=user.email
            )
        return None

    def create(self, user_dto: UserCreateDto) -> UserResponseDto:
        """
        Creates a new user and their associated loyalty account.

        Args:
            user_dto (UserCreateDto): Data transfer object
            containing user data.

        Returns:
            UserResponseDto: The created user's data.
        """

        user: User = User(
            name=user_dto.name,
            email=user_dto.email,
            password=user_dto.password
        )
        created_user: User = self.user_repository.create(user)

        return UserResponseDto(
            id=created_user.id,
            name=created_user.name,
            email=created_user.email
        )

    # def update(self, id: int, user_dto: UserUpdateDto) -> Optional[UserResponseDto]:  # noqa: E501
    #     """
    #     Updates an existing user's data.

    #     Args:
    #         id (int): The ID of the user to update.
    #         user_dto (UserUpdateDto): Data transfer object containing
    #         updated user data.

    #     Returns:
    #         Optional[UserResponseDto]: The updated user's data,
    #         or None if not found.
    #     """
    #     user: Optional[User] = self.user_repository.find_by_id(id)
    #     if user:
    #         if user_dto.name:
    #             user.name = user_dto.name
    #         if user_dto.email:
    #             user.email = user_dto.email
    #         updated_user: User = self.user_repository.update(
    #             user)
    #         return UserResponseDto(
    #             id=updated_user.id,
    #             name=updated_user.name,
    #             email=updated_user.email
    #         )
    #     return None

    def delete(self, id: int) -> None:
        """
        Deletes a user by their ID.

        Args:
            id (int): The ID of the user to delete.
        """
        self.user_repository.delete(id)

    def find_all(self) -> List[UserResponseDto]:
        """
        Retrieves all users and their data.

        Returns:
            List[UserResponseDto]: List of all user data.
        """
        users: List[User] = self.user_repository.find_all()
        return [UserResponseDto(
            id=user.id,
            name=user.name,
            email=user.email
        ) for user in users]
from typing import Optional, List
from app.libs.repositories.base_repository import BaseRepository
from app.modules.user.models.database.user import UserTable
from app.modules.user.models.domain.user import User
from app.modules.user.mappers.user_mapper import UserMapper
from app import db
import logging

logger = logging.getLogger(__name__)


class UserRepository(BaseRepository[UserTable]):
    def __init__(self):
        """
        Initializes the UserRepository with the UserTable model.
        """
        super().__init__(UserTable)

    def find_by_id(self, id: int) -> Optional[User]:
        """
        Retrieves a user by their ID.

        Args:
            id (int): The ID of the user to find.

        Returns:
            Optional[User]: The found user or None if not found.
        """
        user_table: Optional[UserTable] = super().find_by_id(id)
        return (
            UserMapper.from_persistence(user_table)
            if user_table
            else None
        )

    def find_by_email(self, email: str) -> Optional[User]:
        """
        Retrieves a user by their email address.

        Args:
            email (str): The email address to search for.

        Returns:
            Optional[User]: The found user or None if not found.
        """
        user_table = db.session.query(UserTable).filter(
            UserTable.email == email).first()
        return (
            UserMapper.to_domain(user_table)
            if user_table
            else None
        )

    def find_all(self) -> List[User]:
        """
        Retrieves all users.

        Returns:
            List[User]: A list of all User objects.
        """
        user_tables = super().find_all()
        return [
            UserMapper.to_domain(user)
            for user in user_tables
        ]

    def create(self, user: User) -> User:
        """
        Creates a new user.

        Args:
            user (User): The user object to create.

        Returns:
            User: The created User object.
        """
        user_table: UserTable = UserMapper.to_persistence_model(
            user)
        created_user = super().create(user_table)

        return UserMapper.from_persistence(created_user)

    def update(self, user: User) -> User:
        """
        Updates an existing user.

        Args:
            user (User): The user object to update.

        Returns:
            User: The updated User object.
        """
        user_table = UserMapper.to_persistence_model(user)
        updated_user = super().update(user_table)
        return UserMapper.from_persistence(updated_user)

    def delete(self, id: int) -> None:
        """
        Deletes a user by their ID after verifying their existence.

        Args:
            id (int): The ID of the user to delete.
        """
        user = self.find_by_id(id)
        if user:
            try:
                super().delete(id)
            except Exception as e:
                logger.error(f"Error deleting user: {e}")
                raise e
        else:
            logger.error(f"User with ID {id} not found.")
            raise ValueError(f"User with ID {id} not found.")
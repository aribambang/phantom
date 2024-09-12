from app.modules.user.services.user_service import UserService
from app.modules.user.models.domain.user import User
from app.modules.auth.schemas.post_register_schema import (
    PostRegisterDto,
    PostRegisterResponseDto,
)
from app import bcrypt
import logging

logger = logging.getLogger(__name__)

class PostRegisterService:
    """Service layer for handling user-related operations."""

    def __init__(
        self,
        user_service: UserService,
    ):
        """
        Initializes the UserService with required repositories.

        Args:
            user_repository (UserRepository): Repository for user data.
        """
        self.user_service: UserService = user_service
    
    def register(self, user_dto: PostRegisterDto) -> PostRegisterResponseDto:
        """
        Register a new user.

        Args:
            user_dto (PostRegisterDto): Data transfer object
            containing user data.

        Returns:
            PostRegisterDto: The register user's data.
        """
        user_exist = self.user_service.find_by_email(user_dto.email)
        if user_exist:
            raise ValueError("User already exist")
        
        password_hashed: str = bcrypt.generate_password_hash(user_dto.password)
        user: User = User(
            name=user_dto.name,
            email=user_dto.email,
            password=password_hashed
        )
        created_user: User = self.user_service.create(user)

        return PostRegisterResponseDto(
            id=created_user.id,
            name=created_user.name,
            email=created_user.email
        )
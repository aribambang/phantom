import pytest
from unittest.mock import Mock
from app.modules.auth.services.post_register_service import PostRegisterService
from app.modules.auth.schemas.post_register_schema import PostRegisterDto
from app.modules.user.services.user_service import UserService
from app.modules.user.models.domain.user import User
from app.modules.user.schemas.user import UserResponseDto

@pytest.fixture
def post_register_service():
    mock_user_service = Mock()
    return PostRegisterService(
        mock_user_service,
    )

def test_register_with_existing_user(post_register_service):
    # Arrange
    user_dto = PostRegisterDto(
        name= "Bambang", 
        email= "bambang@email.com", 
        password= "xxxxxx"
    )
    mock_user = User(id=1, name="Bambang", email="bambang@email.com")
    post_register_service.user_service.find_by_email.return_value = None
    post_register_service.user_service.user_repository.create.return_value = mock_user

    # Act
    
    result = post_register_service.register(user_dto)

    # Assert
    assert isinstance(result, UserResponseDto)
    assert result.id == 1
    assert result.name == "Bambang"
    assert result.email == "bambang@email.com"
    post_register_service.user_service.create.assert_called_once_with(1)
    post_register_service.user_service.user_repository.create.assert_called_once_with(1)

def test_register_with_existing_user(post_register_service):
    # Arrange
    user_dto = PostRegisterDto(
        name= "Bambang", 
        email= "bambang@email.com", 
        password= "xxxxxx"
    )
    mock_user = User(id=1, name="Bambang", email="bambang@email.com")
    post_register_service.user_service.find_by_email.return_value = (mock_user)

    # Act & Assert
    with pytest.raises(ValueError, match="User already exist"):
        post_register_service.register(user_dto)
    post_register_service.user_service.find_by_email.assert_called_once_with("bambang@email.com")
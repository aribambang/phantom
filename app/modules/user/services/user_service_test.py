import pytest
from unittest.mock import Mock
from app.modules.user.services.user_service import UserService
from app.modules.user.models.domain.user import User
from app.modules.user.schemas.user import UserResponseDto

@pytest.fixture
def user_service():
    mock_user_repository = Mock()
    return UserService(
        mock_user_repository,
    )

def test_find_by_id_existing_user(user_service):
    # Arrange
    mock_user = User(id=1, name="Bambang", email="bambang@email.com")
    user_service.user_repository.find_by_id.return_value = (mock_user)

    # Act
    result = user_service.find_by_id(1)

    # Assert
    assert isinstance(result, UserResponseDto)
    assert result.id == 1

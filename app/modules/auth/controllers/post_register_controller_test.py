import flask
import pytest
from flask import Flask, json
from app.modules.auth.controllers.post_register_controller import bp as auth_bp
from app.modules.user.services.user_service import UserService
from app.modules.auth.services.post_register_service import PostRegisterService
from unittest.mock import Mock

@pytest.fixture
def app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(auth_bp)
    return app

@pytest.fixture
def test_client(app, mocker):
    return app.test_client()

@pytest.fixture
def mock_post_register_service(app, mocker):
    with app.app_context():
        if not hasattr(flask.g, 'container'):
            flask.g.container = Mock()
        mock = Mock(PostRegisterService)
        mocker.patch('flask.g.container.resolve', return_value=mock)
        return mock

def test_register(test_client, app, mocker):
    with app.app_context():
        if not hasattr(flask.g, 'container'):
            flask.g.container = Mock()
        mock_post_register_service = Mock(PostRegisterService)
        mocker.patch('flask.g.container.resolve',
                     return_value=mock_post_register_service)
        # Arrange
        user_data = {'name': 'Bambang', 'email': 'bambang@email.com', 'password': 'xxxxxx'}
        mock_post_register_service.register.return_value = {'id': 1, **user_data}

        # Act
        response = test_client.post('/auth/register', json=user_data)

        # Assert
        assert response.status_code == 201
        assert json.loads(response.data) == {'id': 1, **user_data}
        mock_post_register_service.register.assert_called_once()
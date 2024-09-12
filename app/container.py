from typing import Dict, Any
from flask import g


class Container:
    """Dependency Injection container for managing dependencies."""

    def __init__(self) -> None:
        """Initialize DIContainer with an empty dependencies dict."""
        self._dependencies: Dict[str, Any] = {}

    def register(self, name: str, dependency: Any) -> None:
        """
        Register a dependency.

        Args:
            name (str): The name identifier for the dependency.
            dependency (Any): The dependency instance.
        """
        self._dependencies[name] = dependency

    def resolve(self, name: str) -> Any:
        """
        Resolve a dependency by name.

        Args:
            name (str): The name identifier for the dependency.

        Returns:
            Any: The resolved dependency or None if not found.
        """
        return self._dependencies.get(name)


# Create a global instance of the container
container = Container()

def register_dependencies(app):
    """
    Register all dependencies into the Container and attach it to the app.

    Args:
        app: The Flask application instance.
    """
    from app.modules.user.repositories.user_repository import UserRepository
    from app.modules.user.services.user_service import UserService
    from app.modules.auth.services.post_register_service import PostRegisterService

    # Register repositories
    container.register('user_repository', UserRepository())

    # Register services
    container.register('user_service', UserService(
        container.resolve('user_repository'),
    ))
    container.register('post_register_service', PostRegisterService(
        container.resolve('user_service')
    ))

    # Add the container to the app context
    @app.before_request
    def before_request():
        """Attach the DIContainer to the global object before each request."""
        g.container = container
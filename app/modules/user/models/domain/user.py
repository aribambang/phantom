from typing import Optional

class User:
    def __init__(
        self,
        name: str,
        email: str,
        id: Optional[int] = None,
        password: Optional[str] = None
    ) -> None:
        """
        Initializes a new User instance.

        Args:
            id (int): The unique identifier for the customer.
            name (str): The name of the user.
            email (str): The email address of the user.
            password (str): The password address of the user.
        """
        self.id: Optional[int] = id
        self.name: str = name
        self.email: str = email
        self.password: Optional[str] = password
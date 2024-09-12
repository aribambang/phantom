import json
from tests.base_test import BaseE2ETestCase
from app.modules.user.models.database.user import UserTable
from app.modules.auth.schemas.post_register_schema import PostRegisterDto


class PostRegisterE2ETest(BaseE2ETestCase):
    def test_register_user(self) -> None:
        """Test the creation of a customer via the API."""
        self.list_routes()
        # Arrange
        user_data: PostRegisterDto = PostRegisterDto(
            name="Bambang",
            email="bambang@email.com",
            password="xxxxxx"
        )

        # Act
        response = self.client.post('/auth/register',
                                    data=json.dumps(
                                        user_data.model_dump()),
                                    content_type='application/json')

        # Assert
        self.assertEqual(response.status_code, 201)
        data: dict = json.loads(response.data.decode())
        self.assertIn('id', data)
        self.assertEqual(data['name'], "Bambang")
        self.assertEqual(data['email'], "bambang@email.com")

        # Verify database state
        user: UserTable = UserTable.query.filter_by(
            email="bambang@email.com").first()
        self.assertIsNotNone(user)
        self.assertEqual(user.name, "Bambang")
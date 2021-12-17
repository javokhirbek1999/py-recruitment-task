from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTests(TestCase):
    """User Models tests"""

    def test_create_user_with_email_successfully(self):
        """Test creating users with email is successful"""

        payload = {'email': 'test@gmail.com', 'username': 'testuser123', 'password':'testpass123'}

        user = get_user_model().objects.create_user(
            email=payload['email'],
            username=payload['username'],
            password=payload['password']
        )


        self.assertEqual(user.email, payload['email'])
        self.assertEqual(user.username, payload['username'])
        self.assertTrue(user.check_password(payload['password']))
    
    def test_create_user_email_is_normalized(self):
        """Test email is normalized when creating a user"""

        payload = {'email':'test@gMaIl.com', 'username':'testuser123', 'password':'testpass123'}

        user = get_user_model().objects.create_user(
            email=payload['email'],
            username=payload['username'],
            password=payload['password']
        )

        self.assertEqual(user.email, 'test@gmail.com')
    
    def test_create_admin_user_is_successful(self):
        """Test creating an Admin user is successful"""

        payload = {'email':'test@gmail.com', 'username':'testuser123', 'password': 'testpass123'}

        user = get_user_model().objects.create_superuser(
            email=payload['email'],
            username=payload['username'],
            password=payload['password']
        )

        self.assertTrue(user.is_superuser)
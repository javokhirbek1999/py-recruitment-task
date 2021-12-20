from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework import status



CLIENT_USER_URL = reverse('users:client-users-list')
ADMIN_USER_URL = reverse('users:admin-users-list')

class UserApiTests(TestCase):
    """Tests for User API"""

    def setUp(self):
        self.client = APIClient()
        
    
    def test_create_client_user_api_successul(self):
        """Test creating user through api is successful"""

        payload = {'email': 'testuser@gmail.com', 'username': 'testuser123', 'password': 'testpass123'}

        response = self.client.post(CLIENT_USER_URL, payload)

        user = get_user_model().objects.first()

        self.assertEqual(user.email, payload['email'])
        self.assertEqual(user.username, payload['username'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_admin_user_api_successful(self):
        """Test creating admin user through api is successful"""

        payload = {'email': 'testuser@gmail.com', 'username': 'testuser123', 'password': 'testpass123'}

        response = self.client.post(ADMIN_USER_URL, payload)

        user = get_user_model().objects.get(id=1)
        
        self.assertTrue(user.is_superuser)
        self.assertEqual(user.email, payload['email'])
        self.assertEqual(user.username, payload['username'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_user_password_is_not_in_response_data(self):
        """Test password is not returned in response data when user is created with given credentials"""

        payload = {'email': 'testuser@gmail.com', 'username': 'testuser123', 'password': 'testpass123'}

        response = self.client.post(CLIENT_USER_URL, payload)
        response2 = self.client.post(ADMIN_USER_URL, payload)

        self.assertNotIn(payload['password'], response.data)
        self.assertNotIn(payload['password'], response2.data)
    
    
    
    
    


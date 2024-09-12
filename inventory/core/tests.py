from django.test import TestCase
from django.urls import reverse

class URLTests(TestCase):
    def test_admin_access(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)

    def test_token_obtain(self):
        response = self.client.post(reverse('token_obtain_pair'), {'username': 'yourusername', 'password': 'yourpassword'})
        self.assertEqual(response.status_code, 200)

    def test_token_refresh(self):
        # Add logic to test token refresh if you have a valid token
        pass

    def test_token_verify(self):
        # Add logic to test token verification if you have a valid token
        pass

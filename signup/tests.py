from django.test import TestCase
from django.contrib.auth.models import User


class SignupRedirectTests(TestCase):
    def test_successful_signup_redirects_to_signin(self):
        response = self.client.post(
            "/signup/",
            {
                "firstname": "Ada",
                "lastname": "Lovelace",
                "username": "adalovelace",
                "email": "ada@example.com",
                "password": "secure-pass-123",
                "confirm_password": "secure-pass-123",
                "terms": "on",
            },
        )

        self.assertRedirects(response, "/signin/", fetch_redirect_response=False)
        self.assertTrue(User.objects.filter(username="adalovelace").exists())

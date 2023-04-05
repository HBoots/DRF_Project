""""""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

# TEST NOTES
# get_user_model is a helper function that will retrieve the default user model.  Useful if the default changes.
# example.com is a reserved domain specifically used for testing.  Using any other domain name in testing risks sending actual emails to somebody.

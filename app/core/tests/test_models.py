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

    def test_user_email_normalize(self):
        test_strings = [
            ["Test1@Example.com", "Test1@example.com"],
            ["test2@EXAMPLE.com", "test2@example.com"],
            ["Test3@example.COM", "test3@example.com"],
            ["TEST4@example.com", "test4@example.com"],
        ]

        for entered, expected_result in test_strings:
            user = get_user_model().objects.create_user(
                email=entered,
                password="test_password"
            )

            self.assertEqual(user.email, expected_result)

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
            ["test3@example.COM", "test3@example.com"],
            ["TEST4@example.com", "TEST4@example.com"],
        ]

        for entered, expected_result in test_strings:
            user = get_user_model().objects.create_user(
                email=entered,
                password="test_password"
            )

            self.assertEqual(user.email, expected_result)

    def test_user_email_required(self):
        # user = get_user_model().objects.create_user(
        #     email="",
        #     password="test_password"
        # )

        self.assertRaises(
            ValueError,
            get_user_model().objects.create_user(
                email="",
                password="test_password"
            ))

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test_password'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

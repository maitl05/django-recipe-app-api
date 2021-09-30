from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating a new user with an email is successful"""
        email = 'dummy@dum.dom'
        password = 'dumdumdum'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email for the new user is normalized"""
        email = 'dummy@DUM.COM'
        user = get_user_model().objects.create_user(email, 'randomstring')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''test creating new user with invalid email'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'randompassword')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser('dum@super.user', 'superpassword')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

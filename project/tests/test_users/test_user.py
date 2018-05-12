"""Users tests."""
from django.contrib.auth import get_user_model
from django.test import TestCase

from tests.utils import ModelTestCase
from users.factory import UserFactory

User = get_user_model()


class EmailAuthenticationTest(TestCase):
    """Tests to make sure a user can authenticate with email and password."""

    def test_authenticate_with_email_succeeds(self):
        email, password = 'john.doe@email.net', 'secretpassword'
        user = User.objects.create(email=email)
        user.set_password(password)
        user.save()
        logged_in = self.client.login(email=email, password=password)
        self.assertTrue(logged_in)

    def test_authenticate_with_username_fails(self):
        username = 'johndoe'
        email, password = 'john.doe@email.net', 'secretpassword'
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        logged_in = self.client.login(username=username, password=password)
        self.assertFalse(logged_in)


class UserModelTest(ModelTestCase):
    """Test the user model."""

    model = User
    field_tests = {
        'username': {
            'unique': False,
            'blank': True,
            'null': True,
        },
        'email': {
            'unique': True,
            'blank': False,
            'null': False,
        },
    }
    model_tests = {
        'verbose_name': 'utilisateur',
    }

    @classmethod
    def setUpTestData(self):
        self.obj = UserFactory.create()

    def test_two_users_with_same_username_allowed(self):
        UserFactory.create(username='foo')
        UserFactory.create(username='foo')

    def test_two_users_with_same_email_not_allowed(self):
        same_email = 'same.email@example.net'
        UserFactory.create(email=same_email)
        _, created = User.objects.get_or_create(email=same_email)
        self.assertFalse(created)

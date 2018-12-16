# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .regbackend import EmailLoginBackend


class LoginViewTests(TestCase):

    def test_get_request(self):
        response = self.client.get(reverse("account_login"))
        self.assertEqual(response.status_code, 200)


class RegisterViewTest(TestCase):

    def test_get_request(self):
        response = self.client.get(reverse("account_signup"))
        self.assertEqual(response.status_code, 200)


class PasswordChangeViewTest(TestCase):

    def test_get_request(self):
        response = self.client.get(reverse("account_change_password"))
        self.assertEqual(response.status_code, 302)


class PasswordResetViewTest(TestCase):

    def test_get_request(self):
        response = self.client.get(reverse("account_reset_password"))
        self.assertEqual(response.status_code, 200)


class EmailLoginBackendTests(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'test',
            'email': 'test@email.com',
            'password': 'test@123'}
        self.user = User.objects.create_user(**self.credentials)

    def test_valid_username_login(self):
        response = self.client.login(username=self.credentials['username'],
                                     password=self.credentials['password'])
        self.assertTrue(response)

    def test_invalid_username_login(self):
        response = self.client.login(username='invalid_username',
                                     password=self.credentials['password'])
        self.assertFalse(response)

    def test_valid_email_login(self):
        response = self.client.login(username=self.credentials['email'],
                                     password=self.credentials['password'])
        self.assertTrue(response)

    def test_invalid_email_login(self):
        response = self.client.login(username='invalid_email',
                                     password=self.credentials['password'])
        self.assertFalse(response)

    def test_invalid_password_login(self):
        response = self.client.login(username=self.credentials['email'],
                                     password='incorrect_password')
        self.assertFalse(response)

    def test_valid_get_user(self):
        backend = EmailLoginBackend()
        returned_user = backend.get_user(self.user.id)
        self.assertEqual(returned_user.id, self.user.id)

    def test_invalid_get_user(self):
        backend = EmailLoginBackend()
        # The database has only one user. User with id=10 doesn't exists
        returned_user = backend.get_user(user_id=10)
        self.assertIsNone(returned_user)

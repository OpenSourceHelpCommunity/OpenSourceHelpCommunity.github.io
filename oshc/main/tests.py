# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase, TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    def test_get_request(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)


class RequestSessionViewTests(SimpleTestCase):
    def test_get_request(self):
        response = self.client.get(reverse('request_session'))
        self.assertEqual(response.status_code, 200)

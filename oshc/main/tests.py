# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase
from django.urls import reverse


class HomeViewTests(SimpleTestCase):

    def test_get_request(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

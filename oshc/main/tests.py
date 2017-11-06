# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from main.models import Contest, chatSession
import datetime
from django.utils import timezone
from django.test import Client


class HomeViewTests(TestCase):

    def test_get_request(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)


class RequestSessionViewTests(SimpleTestCase):

    def test_get_request(self):
        response = self.client.get(reverse('request_session'))
        self.assertEqual(response.status_code, 200)


class ChatSessionCreateTestCase(TestCase):
    def setUp(self):
        self.start_date = timezone.make_aware(datetime.datetime(2017, 11, 6, 12, 10, 5))
        self.end_date = timezone.make_aware(datetime.datetime(2017, 12, 15, 22, 45, 50))
        chatSession.objects.create(title="oshc-session", profile_name="test_name", profile_url="http://google.com/", description="This is a sample description",
                                   start_date=self.start_date, end_date=self.end_date, register_url="http://google.com/")

    def test_title(self):
        SessionTitle = chatSession.objects.get(title="oshc-session")
        self.assertEqual(SessionTitle.title, 'oshc-session')

    def test_profile_name(self):
        SessionProfileName = chatSession.objects.get(profile_name="test_name")
        self.assertEqual(SessionProfileName.profile_name, "test_name")

    def test_profile_url(self):
        SessionProfileUrl = chatSession.objects.get(
            profile_url="http://google.com/")
        self.assertEqual(SessionProfileUrl.profile_url, "http://google.com/")

    def test_description(self):
        SessionDescription = chatSession.objects.get(
            description="This is a sample description")
        self.assertEqual(SessionDescription.description,
                         "This is a sample description")

    def test_start_date(self):
        ContestStartDate = chatSession.objects.get(start_date=self.start_date)
        self.assertEqual(ContestStartDate.start_date, self.start_date)

    def test_end_date(self):
        ContestEndDate = chatSession.objects.get(end_date=self.end_date)
        self.assertEqual(ContestEndDate.end_date, self.end_date)

    def test_register_url(self):
        SessionRegisterUrl = chatSession.objects.get(
            register_url="http://google.com/")
        self.assertEqual(SessionRegisterUrl.register_url, "http://google.com/")


class ContestCreateTestCase(TestCase):
    def setUp(self):
        Contest.objects.create(name="oshc", link="http://google.com/", description="This is a sample description",
                               start_date="2014-04-03", end_date="2014-04-04", approved=True)

    def test_name(self):
        ContestName = Contest.objects.get(name="oshc")
        self.assertEqual(ContestName.name, 'oshc')

    def test_link(self):
        ContestLink = Contest.objects.get(link="http://google.com/")
        self.assertEqual(ContestLink.link, "http://google.com/")

    def test_description(self):
        ContestDescription = Contest.objects.get(
            description="This is a sample description")
        self.assertEqual(ContestDescription.description,
                         "This is a sample description")

    def test_start_date(self):
        ContestStartDate = Contest.objects.get(start_date="2014-04-03")
        self.assertEqual(ContestStartDate.start_date,
                         datetime.date(2014, 4, 3))

    def test_end_date(self):
        ContestEndDate = Contest.objects.get(end_date="2014-04-04")
        self.assertEqual(ContestEndDate.end_date, datetime.date(2014, 4, 4))


class ContestCreateValidation(TestCase):
    def test_contest_create(self):
        c = Client()
        response = c.post('/contest_new/', {'name': 'oshc', 'link': 'http://google.com/', 'description': 'This is a sample description', 'start_date': '2014-04-03', 'end_date': '2014-04-04', 'approved': 'True'})
        self.assertEqual(response.status_code, 200)

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.

class ThesisTest(APITestCase):

    fixtures = ['fixtures/user.json', 'fixtures/member.json']

    def test_create_theses(self):
        url = '/theses/'
        data = {'topic': 'the topic', 'title': 'the tittle'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = {'topic': 'the topic', 'title': 'the tittle',
                'student': 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TaskTest(APITestCase):

    fixtures = ['fixtures/user.json',
                'fixtures/member.json',
                'fixtures/progress.json']

    def test_create_task_for_student(self):
        url = '/tasks/'

        data = {'student': 'farhan', 'name': 'tugas baru', 'description': 'membuat tugas',
                'duration': 5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.content)

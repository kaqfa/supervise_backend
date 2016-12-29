from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Template


class TemplateTest(APITestCase):

    fixtures = ['fixtures/user.json', 'fixtures/member.json',
                'fixtures/progress.json']

    def test_create_template(self):
        url = '/templates/'
        self.client.login(username='supervisor', password='qwerty123')
        data = {'name': 'template biasa',
                'description': 'template skripsi seperti biasanya'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         response.content)

        data = {'name': 'template lainnya'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_template(self):
        url = '/templates/1/'
        self.client.login(username='supervisor', password='qwerty123')
        data = {'name': 'template istimewa', 'description': 'template yang istimewa'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)

        data = {'name': 'template biasa aja'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)

    def test_delete_template(self):
        url = '/templates/1/'
        self.client.login(username='supervisor', password='qwerty123')
        # data = {'name': 'template istimewa', 'description': 'template yang istimewa'}
        exist = Template.objects.filter(pk=1)
        self.assertEqual(exist.count(), 1)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.content)
        exist = Template.objects.filter(pk=1)
        self.assertEqual(exist.count(), 0)


class ThesisTest(APITestCase):

    fixtures = ['fixtures/user.json', 'fixtures/member.json']

    def test_create_theses(self):
        url = '/theses/'
        data = {'topic': 'the topic', 'title': 'the tittle'}
        self.client.login(username='supervisor', password='qwerty123')
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
        self.client.login(username='supervisor', password='qwerty123')

        data = {'student': 'farhan', 'name': 'tugas baru', 'description': 'membuat tugas',
                'duration': 5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_student_task(self):
        url = '/tasks/student_task/'
        self.client.login(username='supervisor', password='qwerty123')
        
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)

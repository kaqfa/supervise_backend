from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Application


class TestMother(APITestCase):
    
    def setUp(self):
        app = Application.objects.create(name="Testing App", code="123456")
        self.appkey = app.code


class AppTest(TestMother):
    
    def setUp(self):
        app = Application.objects.create(name="Testing App", code="123456")
        self.appkey = app.code

    def test_create_app(self):
        url = '/rest/g/app/' # reverse('app-register')
        data = {'AppName': 'TestApp'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data['code'], '1')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        app = Application.objects.get(name="TestApp")
        self.assertEqual(app.code, response.data['message'])

    def test_app_exist(self):
        url = '/rest/g/app/'
        data = {'AppName': 'Testing App'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(response.data, {'message': 'appname exists', 'code': '0'})    

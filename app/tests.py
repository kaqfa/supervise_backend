from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Application
from member.models import Member


# class TestMother(APITestCase):

#     def setUp(self):
#         app = Application.objects.create(name="Testing App", code="123456")
#         self.appkey = app.code
#         self.password = 'qwerty123'
#         self.super_token = 'edcba'
#         self.student_token = 'abcde'
#         superv = Member.objects.create(
#                                 username='supervisor', password=self.password,
#                                 npp='55555', name='supervisor',
#                                 email= 'supervisor@gmail.com')
#         self.superv = superv
#         MemberToken.objects.create(member=superv, token=self.super_token, status='a')

#         student = Member.objects.create(
#                                  username='student', password=self.password,
#                                  nim='54321', name='studdent',
#                                  email='student@gmail.com')
#         self.student = student
#         MemberToken.objects.create(member=student, token=self.student_token, status='a')

#     def appkey_valid(self, url):
#         data = {'foo': 'foo'}
#         response = self.client.post(url, data, format="json")
#         self.assertEqual(response.data['message'], 'appkey must present')

#         data = {'appkey': '123'}
#         response = self.client.post(url, data, format="json")
#         self.assertEqual(response.data['message'], 'appkey is not valid')


class AppTest(APITestCase):

    def setUp(self):
        app = Application.objects.create(name="Testing App", code="123456")
        self.appkey = app.code

    def test_create_app(self):
        url = reverse('app-register-list')
        data = {'AppName': 'TestApp'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data['code'], '1')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        app = Application.objects.get(name="TestApp")
        self.assertEqual(app.code, response.data['message'])

    def test_app_exist(self):
        url = reverse('app-register-list')
        data = {'AppName': 'Testing App'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(response.data, {'message': 'appname exists', 'code': '0'})    

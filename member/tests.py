from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from app.tests import TestMother 
from app.models import Application
from .models import Member


class MemberTesting(TestMother):           
    
    def test_login(self):
        url = reverse('app-login-list')
        self.appkey_valid(url)
        data = {'appkey': self.appkey, 'username': 'test', 'password': 'test'}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.data['message'], 'username tidak ditemukan')

    def test_is_username_exists(self):        
        Member.objects.create(username='user', password='pass', status='a',
                              name='user', email='user@email.com')                              
        url = reverse('username-exist-list')

        self.appkey_valid(url)
        data = {'appkey': self.appkey, 'username': 'user'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data['code'], '0')
        self.assertEqual(response.data['message'], 'username already exists!')

        data = {'appkey': self.appkey, 'username': 'andre'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data['code'], '1')
        self.assertEqual(response.data['message'], 'username is available')


class SupervisorTesting(TestMother):

    def test_supervisor_register(self):
        url = reverse('supervisor-register-list')
        self.appkey_valid(url)        

        data = {'appkey': '123456', 'username': 'superve', 'password': 'supervise123', 
                'name': 'super visormu', 'email': 'super@gmail.com',}
        response = self.client.post(url, data, format="json")        
        self.assertEqual(response.data['code'], '0')
        # self.assertEqual(response.data['message']['non_field_errors'][0], 'Pembimbing harus memiliki NPP')
        self.assertContains(response, 'Pembimbing harus memiliki NPP')
        
        data = {'appkey': '123456', 'username': 'superve', 'password': 'supervise123', 
                'npp': '12345', 'name': 'super visormu', 'email': 'super@gmail.com',}
        response = self.client.post(url, data, format="json")        
        self.assertEqual(response.data['code'], '1')
        dbSuper = Member.objects.filter(username='superve').values()[0]
        del dbSuper['supervisor_id']
        del dbSuper['status']
        del dbSuper['id']                
        self.assertEqual(response.data['message'], dbSuper)


class StudentTesting(TestMother):
    
    def test_student_register(self):
        url = reverse('student-register-list')
        self.appkey_valid(url)

        data = {'appkey': '123456', 'username': 'stud', 'password': 'study123', 
                'name': 'stud dentmu', 'email': 'studs@gmail.com',}
        response = self.client.post(url, data, format="json")        
        self.assertEqual(response.data['code'], '0')
        self.assertEqual(response.data['message']['non_field_errors'][0], 
                         'Mahasiswa harus memiliki NIM')        

        data = {'appkey': '123456', 'username': 'stud', 'password': 'study123', 
                'nim': '12345', 'name': 'stud dentmu', 'email': 'studs@gmail.com',}
        response = self.client.post(url, data, format="json")        
        self.assertEqual(response.data['code'], '1')
        dbSuper = Member.objects.filter(username='stud').values()[0]
        del dbSuper['supervisor_id']
        del dbSuper['status']
        del dbSuper['id']                
        self.assertEqual(response.data['message'], dbSuper)

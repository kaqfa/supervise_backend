from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from app.tests import TestMother 
from app.models import Application


class MemberTesting(TestMother):

    def test_appkey_valid(self):        
        url = reverse('app-login-list')
        data = {'username': 'test', 'password': 'test'}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.data['message'], 'appkey must present')

        data = {'appkey': '123', 'username': 'test', 'password': 'test'}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.data['message'], 'appkey is not valid')        
    
    def test_login(self):
        url = reverse('app-login-list')
        data = {'appkey': self.appkey, 'username': 'test', 'password': 'test'}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.data['message'], 'username tidak ditemukan')


class SupervisorTesting(TestMother):

    def test_supervisor_register(self):
        pass
from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status


class AppTest(APITestCase):

    def test_create_app(self):
        url = '/rest/g/app/' # reverse('app-register')
        data = {'AppName': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data['code'], '1')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)        

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
# from app.tests import TestMother 
from app.models import Application
from .models import Member
from progress.models import StudentTask
from django.contrib.auth.models import User
from collections import Counter


class MemberTesting(APITestCase):
    
#     def test_login(self):
#         url = reverse('app-login-list')
#         self.appkey_valid(url)
#         data = {'appkey': self.appkey, 'username': 'test', 'password': 'test'}
#         response = self.client.post(url, data, format="json")
#         self.assertEqual(response.data['message'], 'username tidak ditemukan')

    def test_supervisor_register(self):
        url = reverse('member-register-list')
        # self.appkey_valid(url)

        data = {'appkey': '123456', 'username': 'superve', 'password': 'supervise123',
                'name': 'super visormu', 'level': 'sp', 'email': 'super@gmail.com',
                'address': 'asdf'}
        response = self.client.post(url, data, format="json")
        # self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertContains(response, 'Pembimbing harus memiliki NPP')

        data = {'appkey': '123456', 'username': 'superve', 'password': 'supervise123',
                'npp': '12345', 'name': 'super visormu', 'level': 'sp', 'address': 'asdf',
                'email': 'super@gmail.com'}
        response = self.client.post(url, data, format="json")
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        superv = Member.objects.filter(user__username='superve').values()[0]
        self.assertEqual(superv['npp'], data['npp'])
    
    def test_student_register(self):
        url = reverse('member-register-list')
        # self.appkey_valid(url)

        data = {'appkey': '123456', 'username': 'stud', 'password': 'study123',
                'name': 'stud dentmu', 'level': 'st', 'email': 'studs@gmail.com',
                'address': 'asdf'}
        response = self.client.post(url, data, format="json")
        # self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['non_field_errors'][0],
                         'Mahasiswa harus memiliki NIM')

        data = {'appkey': '123456', 'username': 'stud', 'password': 'study123', 
                'nim': '12345', 'name': 'stud dentmu', 'level': 'st',
                'address': 'asdf', 'email': 'studs@gmail.com',}
        response = self.client.post(url, data, format="json")        
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        student = Member.objects.filter(user__username='stud').values()[0]
        self.assertEqual(student['nim'], data['nim'])

    def test_is_username_exists(self):
        user = User.objects.create(username='user', password='pass',
                                   email='user@email.com', first_name="stud")
        Member.objects.create(user=user, nim='123', level="st")
        url = '/app/members/user/' # reverse('member-list-list', kwargs={'username': 'user'})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data, 1, response.data)
        # self.assertEqual(response.data['data']['user']['username'], 'user')


class SupervisorTesting(APITestCase):

    fixtures = ['fixtures/user.json', 'fixtures/member.json']

    def test_supervisor_list(self):
        login = self.client.login(username='supervisor', password='qwerty123')
        url = reverse('student-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)

    def test_supervisor_detail(self):
        login = self.client.login(username='supervisor', password='qwerty123')
        url = '/supervisors/5/' # reverse('student-detail', kwargs={'id': '5'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        url = '/supervisors/3/' #reverse('student-detail', kwargs={'id': '2'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)

    def test_supervisor_edit_profile(self):
        pass
        # url = reverse('supervisor-edit-profile-list')
        # self.appkey_valid(url)

        # data = {'appkey': self.appkey, 'token': self.super_token,
        #         'address': 'jl. Raya berubah'}
        # response = self.client.post(url, data, format='json')
        # self.assertEqual(response.data['code'], '1', response.data)
        # superv = Member.objects.filter(username='supervisor').values()[0]
        # self.assertEqual(superv['address'], data['address'], superv)

        # data = {'appkey': self.appkey, 'token': self.super_token,
        #         'address': 'jl. Raya berubah', 'handphone': '0999999',
        #         'email': 'berubah@mail.com'}
        # response = self.client.post(url, data, format='json')
        # self.assertEqual(response.data['code'], '1')
        # superv = Member.objects.filter(username='supervisor').values()[0]
        # self.assertEqual(superv['email'], data['email'])


class StudentTesting(APITestCase):

    fixtures = ['fixtures/user.json', 'fixtures/member.json', 'fixtures/progress.json']

    def test_student_detail(self):
        login = self.client.login(username='supervisor', password='qwerty123')
        url = '/students/110/' # reverse('student-detail', kwargs={'id': '5'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        url = '/students/2/' #reverse('student-detail', kwargs={'id': '2'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)

    def test_student_propose(self):
        login = self.client.login(username='farhan', password='qwerty123')
        url = '/students/propose/'

        data = {'supervisor': '5'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = {'supervisor': '4'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_input_code(self):
        login = self.client.login(username='farhan', password='qwerty123')
        url = '/students/input_code/'

        data = {'code': '12345'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.content)
        user = User.objects.get(username='farhan')
        tasks = user.member.studenttask_set.all()
        self.assertEqual(tasks.count(), 7, tasks)

        data = {'code': 'qwerty'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST,
                         response.content)


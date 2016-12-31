from django.db import models
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
import progress


class Expertise(models.Model):
    """Bidang keahlian supervisor"""
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    """Pengganti User, include student dan supervisor"""
    LEVEL_CHOICES = (('st', 'mahasiswa'), ('sp', 'pembimbing'))
    STATUS_CHOICES = (('a', 'aktif'), ('b', 'banned'), ('n', 'nonaktif'),
                      ('g', 'lulus'))

    user = models.OneToOneField(User)
    nim = models.CharField(max_length=20, null=True, blank=True)
    npp = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    expertise = models.ManyToManyField(Expertise, blank=True)
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    status = models.CharField(max_length=1, default='a', choices=STATUS_CHOICES)
    supervisor = models.ForeignKey("self", null=True, blank=True)

    def __str__(self):
        return self.user.username

    def name(self):
        return self.user.first_name+" "+self.user.last_name

    def get_progress_data(self):
        try:
            thesis = {'topic': self.thesis.topic, 'title': self.thesis.title,
                      'abstract': self.thesis.abstract, 'field': None,
                      'save_date': self.thesis.save_date}
            data = {'username': self.user.username, 'nim': self.nim,
                    'name': self.name(), 'thesis': thesis,
                    'number_of_task': self.student_num_of_task(),
                    'number_of_task_done': self.student_num_of_done_task()}
        except progress.models.Thesis.DoesNotExist:
            data = {'username': self.user.username, 'nim': self.nim,
                    'name': self.name(), 'thesis': None,
                    'number_of_task': self.student_num_of_task(),
                    'number_of_task_done': self.student_num_of_done_task()}

        return data

    def student_num_of_task(self):
        if self.level == 'st':
            return self.studenttask_set.all().count()
        return 0

    def student_num_of_done_task(self):
        if self.level == 'st':
            return self.studenttask_set.filter(status=2).count()


class StudentProposal(models.Model):
    STATUS_CHOICES = (('p', 'menunggu'), ('a', 'diterima'), ('r', 'ditolak'))

    student = models.ForeignKey(Member, related_name='%(class)s_student')
    supervisor = models.ForeignKey(Member, related_name='%(class)s_supervisor')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    propose_date = models.DateTimeField(auto_now_add=True)
    response_date = models.DateTimeField(auto_now=True)

    def response(self, code):
        self.status = code
        self.save()

        if code == 'a':
            student = self.student
            student.supervisor = self.supervisor
            student.save()

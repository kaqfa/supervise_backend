from django.db import models
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


class Expertise(models.Model):
    """Bidang keahlian supervisor"""
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)


class Member(models.Model):
    """Pengganti User, include student dan supervisor"""
    LEVEL_CHOICES = (('st', 'mahasiswa'), ('sp', 'pembimbing'))
    STATUS_CHOICES = (('a', 'aktif'), ('b', 'banned'), ('n', 'nonaktif'))
    
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


class StudentProposal(models.Model):
    STATUS_CHOICES = (('p', 'menunggu'), ('a', 'diterima'), ('r', 'ditolak'))

    student = models.ForeignKey(Member, related_name='%(class)s_student')
    supervisor = models.ForeignKey(Member, related_name='%(class)s_supervisor')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    propose_date = models.DateTimeField(auto_now_add=True)
    response_date = models.DateTimeField(auto_now=True)

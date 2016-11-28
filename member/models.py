from django.db import models


class Expertise(models.Model):
    """Bidang keahlian supervisor"""
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)


class Member(models.Model):
    """Pengganti User, include student dan supervisor"""
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    nim = models.CharField(max_length=20, null=True)
    npp = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=50)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=200)
    expertise = models.ManyToManyField(Expertise, null=True)
    level = models.CharField(max_length=2, default='st')
    status = models.CharField(max_length=1, default='a')    


class MemberToken(models.Model):
    """Token untuk login"""
    member = models.ForeignKey(Member)
    token = models.CharField(max_length=20)
    status = models.CharField(max_length=1)
    
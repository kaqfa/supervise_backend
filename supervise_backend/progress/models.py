from django.db import models
from member.models import Member, Expertise 


class MediaFile(models.Model):
    filename = models.FileField()
    by = models.ForeignKey(Member)
    upload_date = models.DateField()


class Thesis(models.Model):
    topic = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    abstract = models.TextField(null=True)
    student = models.ForeignKey(Member)
    field = models.ManyToManyField(Expertise)
    files = models.ManyToManyField(MediaFile)
    save_date = models.DateField()


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    duration = models.SmallIntegerField()
    files = models.ManyToManyField(MediaFile)


class Template(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    task = models.ManyToManyField(Task)
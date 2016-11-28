from django.db import models
from member.models import Member, Expertise


class MediaFile(models.Model):
    filename = models.FileField()
    by = models.ForeignKey(Member)
    upload_date = models.DateField(auto_now_add=True)


class Thesis(models.Model):
    topic = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    abstract = models.TextField(null=True)
    student = models.ForeignKey(Member)
    field = models.ManyToManyField(Expertise, null=True)
    files = models.ManyToManyField(MediaFile, null=True)
    save_date = models.DateField(auto_now_add=True)


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    duration = models.SmallIntegerField()
    files = models.ManyToManyField(MediaFile, null=True)


class Template(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    task = models.ManyToManyField(Task, null=True)


class StudentTask(models.Model):
    student = models.ForeignKey(Member)
    task = models.ForeignKey(Task)
    status = models.CharField(max_length=1, default='1')
    created_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()


class Comment(models.Model):
    by = models.ForeignKey(Member)
    type = models.CharField(max_length=1, default='1')
    text = models.TextField()
    file = models.ManyToManyField(MediaFile, null=True)
    post_date = models.DateField(auto_now_add=True)
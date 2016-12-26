from django.db import models
from member.models import Member, Expertise
from datetime import datetime, timedelta


class MediaFile(models.Model):
    filename = models.FileField()
    by = models.ForeignKey(Member)
    upload_date = models.DateField(auto_now_add=True)


class Thesis(models.Model):
    topic = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    abstract = models.TextField(null=True)
    student = models.ForeignKey(Member)
    field = models.ManyToManyField(Expertise, blank=True)
    files = models.ManyToManyField(MediaFile, blank=True)
    save_date = models.DateField(auto_now_add=True)


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    duration = models.SmallIntegerField()
    files = models.ManyToManyField(MediaFile, blank=True)

    def num_of_files(self):
        return self.files.all().count()

    def __str__(self):
        return self.name


class Template(models.Model):
    supervisor = models.ForeignKey(Member, null=True)
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    task = models.ManyToManyField(Task, through="TemplateTask", blank=True)

    def assign(self, student_id):
        student = Member.objects.get(pk=student_id)
        tasks = self.task.all()
        for data in tasks:
            enddate = datetime.now()+timedelta(days=data.duration)
            StudentTask.objects.create(student=student, task=data,
                                       end_date=enddate)

    def num_of_task(self):
        return self.task.all().count()


class TemplateTask(models.Model):
    template = models.ForeignKey(Template)
    task = models.ForeignKey(Task)
    order = models.SmallIntegerField()


class StudentTask(models.Model):
    student = models.ForeignKey(Member)
    task = models.ForeignKey(Task)
    status = models.CharField(max_length=1, default='1')
    created_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()


class Comment(models.Model):
    by = models.ForeignKey(Member)
    student_task = models.ForeignKey(StudentTask, null=True)
    type = models.CharField(max_length=1, default='1')
    text = models.TextField()
    file = models.ManyToManyField(MediaFile)
    post_date = models.DateField(auto_now_add=True)
    
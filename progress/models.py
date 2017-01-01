from django.db import models
from django.contrib.auth.models import User

from member.models import Member, Expertise
from datetime import datetime, timedelta


class MediaFile(models.Model):
    filename = models.FileField()
    by = models.ForeignKey(Member)
    upload_date = models.DateField(auto_now_add=True)


class Thesis(models.Model):
    topic = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    abstract = models.TextField(null=True, blank=True)
    student = models.OneToOneField(Member)
    field = models.ManyToManyField(Expertise, blank=True)
    files = models.ManyToManyField(MediaFile, blank=True)
    save_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def supervisor(self):
        return self.student.supervisor.user.username


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
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    task = models.ManyToManyField(Task, through="TemplateTask", blank=True)

    def assign(self, user):
        user = User.objects.get(pk=user)
        student = Member.objects.get(user=user)
        tasks = self.task.all()
        for data in tasks:
            enddate = datetime.now()+timedelta(days=data.duration)
            StudentTask.objects.create(student=student, task=data,
                                       end_date=enddate)
        return True

    def num_of_task(self):
        return self.task.all().count()

    def __str__(self):
        return self.supervisor.user.username+"-"+self.name


class TemplateTask(models.Model):
    template = models.ForeignKey(Template)
    task = models.ForeignKey(Task)
    order = models.SmallIntegerField()


class StudentTask(models.Model):
    STATUS_CHOICE = (('1', 'belum dikerjakan'), ('2', 'selesai'),
                     ('3', 'sudah dikerjakan'), ('4', 'kerjakan kembali'))

    student = models.ForeignKey(Member)
    task = models.ForeignKey(Task, null=True, blank=True)
    name = models.CharField(max_length=100, default='')
    description = models.TextField(null=True)
    duration = models.SmallIntegerField(default=1)
    files = models.ManyToManyField(MediaFile, blank=True)
    status = models.CharField(max_length=1, default='1', choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True)

    def save(self, *args, **kwargs):
        if not self.pk and self.task != None:
            self.name = self.task.name
            self.description = self.task.description
            self.duration = self.task.duration

        super(StudentTask, self).save(*args, **kwargs)


class Comment(models.Model):
    TYPE_CHOICE = (('w', 'pengerjaan'), ('e', 'penjelasan'),
                   ('q', 'pertanyaan'))

    by = models.ForeignKey(Member)
    student_task = models.ForeignKey(StudentTask, null=True)
    type = models.CharField(max_length=1, default='w', choices=TYPE_CHOICE)
    text = models.TextField()
    file = models.ManyToManyField(MediaFile, blank=True)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text

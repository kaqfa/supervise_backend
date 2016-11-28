from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)

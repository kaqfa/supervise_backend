from django.db import models
from django.utils.crypto import get_random_string


class Application(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)

    @staticmethod
    def register_application(appname):
        
        if Application.objects.filter(name=appname).count() > 0:
            return False; 
        
        appkey = get_random_string(length=32)
        
        while Application.objects.filter(code=appkey).count() > 0:
            appkey = get_random_string(length=32)            

        Application.objects.create(name=appname,code=appkey)
        return appkey
from django.contrib import admin
from .models import Application
from member.models import Member

admin.site.register(Application)
admin.site.register(Member)
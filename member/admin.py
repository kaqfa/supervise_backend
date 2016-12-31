from django.contrib import admin
from .models import Member, Expertise

class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'nim', 'npp', 'address', 'phone',
                    'level', 'status', 'supervisor')

class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Member, MemberAdmin)
admin.site.register(Expertise, ExpertiseAdmin)
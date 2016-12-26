from django.contrib import admin
from .models import Template, Task, StudentTask, Thesis, MediaFile


class FileInline(admin.StackedInline):
    model = Task.files.through


class TaskInline(admin.TabularInline):
    model = Template.task.through

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('supervisor', 'code', 'name', 'description', 'num_of_task')
    inlines = [TaskInline]


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'duration', 'num_of_files')
    inlines = [FileInline]

admin.site.register(Template, TemplateAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(StudentTask)
admin.site.register(Thesis)
admin.site.register(MediaFile)

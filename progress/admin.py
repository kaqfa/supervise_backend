from django.contrib import admin
from .models import Template, Task, StudentTask, Thesis, MediaFile, Comment


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


class CommentInline(admin.TabularInline):
    model = Comment


class StudentTaskAdmin(admin.ModelAdmin):
    list_display = ('student', 'task', 'status', 'end_date')
    inlines = [CommentInline]


class ThesisAdmin(admin.ModelAdmin):
    list_display = ('student', 'supervisor', 'topic', 'title', 'save_date')

admin.site.register(Template, TemplateAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(StudentTask, StudentTaskAdmin)
admin.site.register(Thesis, ThesisAdmin)
admin.site.register(MediaFile)

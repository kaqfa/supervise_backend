from rest_framework import serializers
from .models import Thesis, Task, Template, StudentTask
from member.models import User
from member.serializers import UserSerializer
from datetime import datetime, timedelta

class ThesisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thesis
        fields = ('topic', 'title', 'abstract', 'student',
                  'field', 'files', 'save_date')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'description', 'duration', 'files')


class StudentTaskSerializer(serializers.ModelSerializer):
    task = TaskSerializer()

    class Meta:
        model = StudentTask
        fields = ('student', 'task', 'status', 'created_date', 'end_date')


class FormStudentTaskSerializer(serializers.Serializer):
    student = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    files = serializers.FileField(required=False, allow_empty_file=True, allow_null=True)

    def create(self, validated_data):
        username = validated_data.get('student')
        name = validated_data.get('name')
        description = validated_data.get('description')
        duration = validated_data.get('duration')
        files = validated_data.get('file', None)

        task = Task.objects.create(name=name, description=description,
                                   duration=duration)
        if files != None:
            for file in files:
                task.files.add(file)

        student = User.objects.get(username=username)
        end_date = datetime.now()+timedelta(days=validated_data.get('duration'))
        StudentTask.objects.create(task=task, student=student.member,
                                   end_date=end_date)

        result = {'student': username, 'name': name, 'description': description,
                  'duration': duration}
        return result

from rest_framework import serializers
from .models import Thesis, Task, Template, StudentTask, Comment
from member.models import User, Member
from member.serializers import UserSerializer
from datetime import datetime, timedelta

import uuid

class ThesisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thesis
        fields = ('topic', 'title', 'abstract', 'student',
                  'field', 'files', 'save_date')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('student_task', 'by', 'type', 'text', 'file', 'post_date')


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('name', 'description', 'duration', 'files')


class TemplateSerializer(serializers.ModelSerializer):
    task = TaskSerializer(many=True, required=False)
    code = serializers.CharField(max_length=5, required=False)

    class Meta:
        model = Template
        fields = ('supervisor', 'code', 'name',
                  'description', 'task')

    def create(self, validated_data):
        data = {'code': uuid.uuid4().hex[:5],
                'supervisor': Member.objects.get(user=self.context['request'].user),
                'name': validated_data.get('name'),
                'description': validated_data.get('description', None)}
        if Template.objects.filter(code=data['code']).count() > 0:
            data['code'] = uuid.uuid4().hex[:5]
        template = Template.objects.create(**data)
        tasks = validated_data.get('task', None)
        if tasks != None:
            for data in tasks:
                template.task.add(data)
        return template

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        # tasks = validated_data.get('task', None)
        # for data in tasks:
        #     task = Task.objects.create(name=data.name, description=data.description,
        #                                duration=data.duration)
        #     instance.task.add(task)
        return instance


class StudentTaskSerializer(serializers.ModelSerializer):
    # task = TaskSerializer(allow_null=True)
    comment_set = CommentSerializer(many=True, allow_null=True)

    class Meta:
        model = StudentTask
        fields = ('student', 'status', 'comment_set', 'created_date', 'end_date')


class StudentProgressSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    nim = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=50)
    thesis = ThesisSerializer
    number_of_task = serializers.IntegerField()
    number_of_done = serializers.IntegerField()


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

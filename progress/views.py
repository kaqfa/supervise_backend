"""View untuk handling request penugasan dan progress"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route, list_route

from .models import Thesis, Task, Template, StudentTask
from .serializers import ThesisSerializer, TaskSerializer, TemplateSerializer
from .serializers import StudentTaskSerializer, FormStudentTaskSerializer
from .serializers import CommentSerializer
from member.models import Member
from rest_framework.permissions import IsAuthenticated


class TemplateViewsets(viewsets.ModelViewSet):
    serializer_class = TemplateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Template.objects.filter(supervisor__user=self.request.user)


class ThesisViewsets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Thesis.objects.all()
    serializer_class = ThesisSerializer


class StudentTaskViewsets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # member = Member.objects.get(user=self.request.user)
        return StudentTask.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return FormStudentTaskSerializer
        return StudentTaskSerializer

    @list_route(methods=['get'])
    def student_task(self, request):
        """Menampilkan semua task yang diberikan pada student.
        Berbeda dengan list yang menampilkan semua student task
        milik semua student"""
        student = Member.objects.get(user=self.request.user)
        studenttasks = StudentTask.objects.filter(student=student)
        task = StudentTaskSerializer(studenttasks, many=True)
        return Response(task.data)

    @detail_route(methods=['post'])
    def comment(self, request, pk):
        student_task = StudentTask.objects.get(pk=pk)
        data = {'student_task': student_task.pk, 'by': request.user.member.id,
                'type': request.data['type'], 'text': request.data['text']}
        comment = CommentSerializer(data=data)
        if comment.is_valid():
            comment.save()
        return Response(comment.data, status=status.HTTP_201_CREATED)

    @detail_route(methods=['put'])
    def validate(self, request, pk):
        student_task = StudentTask.objects.get(pk=pk)
        student_task.status = '2'
        student_task.save()
        serialize = StudentTaskSerializer(student_task)
        return Response(serialize.data)

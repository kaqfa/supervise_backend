"""View untuk handling request penugasan dan progress"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route

from .models import Thesis, Task, Template, StudentTask
from .serializers import ThesisSerializer, TaskSerializer, TemplateSerializer
from .serializers import StudentTaskSerializer, FormStudentTaskSerializer
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
        member = Member.objects.get(user=request.user)
        return StudentTask.objects.filter(student=member)

    def get_serializer_class(self):
        if self.action == 'create':
            return FormStudentTaskSerializer
        return StudentTaskSerializer

    @list_route(methods=['get'])
    def student_task(self, request):
        student = Member.objects.get(user=self.request.user)
        studenttasks = StudentTask.objects.filter(student=student)
        task = StudentTaskSerializer(studenttasks, many=True)
        return Response(task.data)

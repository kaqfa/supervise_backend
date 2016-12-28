"""View untuk handling request penugasan dan progress"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Thesis, Task, Template, StudentTask
from .serializers import ThesisSerializer, TaskSerializer, TemplateSerializer
from .serializers import StudentTaskSerializer, FormStudentTaskSerializer
from member.models import Member


class TemplateViewsets(viewsets.ModelViewSet):
    serializer_class = TemplateSerializer

    def get_queryset(self):
        return Template.objects.filter(supervisor__user=self.request.user)


class ThesisViewsets(viewsets.ModelViewSet):
    queryset = Thesis.objects.all()
    serializer_class = ThesisSerializer


class StudentTaskViewsets(viewsets.ModelViewSet):    

    def get_queryset(self):
        member = Member.objects.get(user=request.user)
        return StudentTask.objects.filter(student=member)

    def get_serializer_class(self):
        if self.action == 'create':
            return FormStudentTaskSerializer
        return StudentTaskSerializer


@api_view(['GET'])
def get_task(request):
    """*appkey, *token, *student, *id_task"""
    return Response({'code':'1', 'message':'the message', 'data':'the task'})

@api_view(['POST'])
def create_task(request):
    """*appkey, *token, *student, *name, description, duration, file"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def update_task(request):
    """*appkey, *token, *student, *id_task, *name, description, duration, remove [array], file"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def delete_task(request):
    """*appkey, *token, *student, *id_task"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def validate_task(request):
    """*appkey, *token, *student, *id_task"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def create_comment(request):
    """*appkey, *token, *student, *id_task, *type, text, file"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def delete_comment(request):
    """*appkey, *token, *student, *id_task, *id_comment"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def create_work(request):
    """*appkey, *token, *student, *id_task, file"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['GET'])
def student_progress(request):
    """*appkey, *token"""
    return Response({'code':'1', 'message':'the message', 'data':'progress data'})

@api_view(['POST'])
def create_template(request):
    """*appkey, *token, *name, description"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def update_template(request):
    """*appkey, *token, *code, *name, description"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def delete_template(request):
    """*appkey, *token, *code"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def submit_final(request):
    """*appkey, *token, *file"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def validate_final(request):
    """*appkey, *token, *student, *code"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def add_template_task(request):
    """*appkey, *token, *template, *id_task, *name, description, duration, file"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def edit_template_task(request):
    """*appkey, *token, *template, *old_name, *new_name, description, duration, remove[], file"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def del_template_task(request):
    """*appkey, *token, *template, *id_task"""
    return Response({'code':'1', 'message':'the message'})
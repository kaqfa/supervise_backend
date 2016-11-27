"""View untuk handling request penugasan dan progress"""

from rest_framework.decorators import api_view
from rest_framework.response import Response


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
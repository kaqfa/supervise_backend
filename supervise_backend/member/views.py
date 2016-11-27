"""View untuk handling request student dan supervisor"""

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def student_register(request):
    """*appkey, *username, *password, *nim, *name, address, handphone, email"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def supervisor_register(request):
    """*appkey, *username, *password, *npp, *name, address, handphone, email"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['GET'])
def get_student(request):
    """*username, *appkey, *token"""
    return Response({'code':'1', 'message':'the message', 'data':'student data'})

@api_view(['GET'])
def get_all_students(request):
    """*appkey, *token"""
    return Response({'code':'1', 'message':'the message', 'data':'students data'})

@api_view(['GET'])
def get_all_supervisors(request):
    """*appkey, *token"""
    return Response({'code':'1', 'message':'the message', 'data':'supervisors data'})

@api_view(['GET'])
def get_supervisor(request):
    """*username, *appkey, *token"""
    return Response({'code':'1', 'message':'the message', 'data':'supervisor data'})

@api_view(['POST'])
def save_thesis(request):
    """*appkey, *token, *topic, *title, *description, *field [array]"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def student_propose(request):
    """*appkey, *token, *supervisor"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def input_code(request):
    """*appkey, *token, *code"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def respond_proposal(request):
    """*appkey, *token, *student, *code"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def save_expertise(request):
    """*appkey, *token, *name, description"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def delete_expertise(request):
    """*appkey, *token, *name"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def is_student_supervisor(request):
    """*appkey, *token, *student"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def student_profile(request):
    """*appkey, *token, address, handphone, email"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def supervisor_profile(request):
    """*appkey, *token, address, handphone, email, *field[]"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def is_username_exist(request):
    """*appkey, *username"""
    return Response({'code':'1', 'message':'the message'})

@api_view(['POST'])
def login(request):
    """*appkey, *username, *password"""
    return Response({'code':'1', 'message':'the message',
                     'username':'the user', 'token':'the token'})

@api_view(['GET'])
def search_by_expertise(request):
    """*appkey, *token, *keysearch"""
    return Response({'code':'1', 'message':'the message', 'data':'the supervisors'})

@api_view(['GET'])
def graduated_student(request):
    """*appkey, *username, *supervisor"""
    return Response({'code':'1', 'message':'the message', 'data':'the students'})

@api_view(['GET'])
def ungraduated_student(request):
    """*appkey, *username, *supervisor"""
    return Response({'code':'1', 'message':'the message', 'data':'the students'})

@api_view(['POST'])
def reset_password(request):
    """*appkey, *token, *old_password, *new_password"""
    return Response({'code':'1', 'message':'the message',
                     'username':'the user', 'token':'the token'})

@api_view(['GET'])
def get_username(request):
    """*appkey, *token"""
    return Response({'code':'1', 'message':'the message', 'data':'user: student / supervisor'})

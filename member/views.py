"""View untuk handling request student dan supervisor"""

from rest_framework.decorators import api_view, list_route
from rest_framework.response import Response
from rest_framework import viewsets
from app.models import Application
from .serializers import RegisterSerializer
from member.models import Member, MemberToken


class StudentRegister(viewsets.ViewSet):
    """API untuk pendaftaran mahasiswa"""
    def create(self, request):
        """Endpoint API untuk pendaftaran mahasiswa"""
        try:
            Application.objects.get(code=request.data['appkey'])
        except KeyError:
            return Response({'code':'0', 'message':'appkey must present'})
        except Application.DoesNotExist:
            return Response({'code':'0', 'message':'appkey is not valid'})

        del request.data['appkey']
        request.data['level']='st'
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'code':'1', 'message':serializer.data})
        else:
            return Response({'code':'0', 'message':serializer.errors})

# @api_view(['POST'])
# def student_register(request):
#     """*appkey, *username, *password, *nim, *name, address, handphone, email"""
#     serializer = RegisterSerializer(request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'code':'1', 'message':serializer})
#     else:
#         return Response({'code':'0', 'message':'something wrong'})


class SupervisorRegister(viewsets.ViewSet):
    """API untuk pendaftaran pembimbing"""
    def create(self, request):
        """Endpoint API untuk pendaftaran pembimbing"""
        try:
            Application.objects.get(code=request.data['appkey'])
        except Application.DoesNotExist:
            return Response({'code':'0', 'message':'appkey is not valid'})

        del request.data['appkey']
        request.data['level'] = 'sp'
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'code':'1', 'message':serializer.data})
        else:
            return Response({'code':'0', 'message':serializer.errors})

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


class Login(viewsets.ViewSet):

    # @list_route(methods=['post'])
    def create(self, request):
        try:
            Application.objects.get(code=request.data['appkey'])
        except KeyError:
            return Response({'code':'0', 'message':'appkey must present'})
        except Application.DoesNotExist:
            return Response({'code':'0', 'message':'appkey is not valid'})
        
        try:                                    
            member = Member.objects.get(username=request.data['username'])        
        except Member.DoesNotExist:
            return Response({'code':'0', 'message':'username tidak ditemukan'})

        if member.check_password(request.data['password']):
            token = MemberToken.create_token(member)
            return Response({'code':'1', 'message':token})
        else:
            return Response({'code':'0', 'message':{'pass':member.password, 
                            'mess': member.check_password(request.data['password'])}})

# @api_view(['POST'])
# def login(request):
#     """*appkey, *username, *password"""
#     return Response({'code':'1', 'message':'the message',
#                      'username':'the user', 'token':'the token'})

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

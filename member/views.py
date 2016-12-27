"""View untuk handling request student dan supervisor"""

from rest_framework.decorators import api_view, list_route
from rest_framework.response import Response
from rest_framework import viewsets, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route, list_route
from app.models import Application
from app.views import AppKeyMixin, app_key_required
from .serializers import RegisterSerializer, ProfileSerializer
from .serializers import UserSerializer, ProposalSerializer
from member.models import Member, User, StudentProposal
from progress.models import StudentTask, Template


class UserViewsets(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class MemberList(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        member = Member.objects.filter(user__username=username)
        return member


class RegisterViewset(AppKeyMixin, viewsets.ViewSet):
    """API untuk registrasi pengguna"""

    def create(self, request):
        """Endpoint API untuk pendaftaran mahasiswa"""
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data)
        else:
            return Response(serializer.errors)


class StudentViewsets(viewsets.ModelViewSet):
    queryset = Member.objects.filter(level='st')
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    @list_route(methods=['post'])
    def propose(self, request):
        student = Member.objects.get(user=request.user)
        supervisor = Member.objects.get(pk=request.data['supervisor'])
        if supervisor.level == 'sp':
            proposal = StudentProposal.objects.create(student=student,
                                                      supervisor=supervisor,
                                                      status='p')
            serializer = ProposalSerializer(proposal)
            return Response({'message': '1'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'pembimbing harus berlevel supervisor'},
                            status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['post'])
    def input_code(self, request):
        try:
            template = Template.objects.get(code=request.data['code'])
            template.assign(request.user.id)
            return Response({'message': '1'})
        except Template.DoesNotExist:
            return Response({'message': 'kode template tidak tepat'},
                            status=status.HTTP_400_BAD_REQUEST)

class SupervisorViewsets(viewsets.ModelViewSet):
    queryset = Member.objects.filter(level='sp')
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


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


class SupervisorProfile(AppKeyMixin, viewsets.ViewSet):

    def create(self, request):
        invalid = self.appkey_check(request.data)
        if invalid:
            return invalid

        # token = MemberToken.objects.get(token=request.data['token'])
        serializer = ProfileSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'code':'1', 'message':serializer.data})
        else:
            return Response({'code':'0', 'message':serializer.errors})
        return Response({'code':'1', 'message':'the message'})


class UsernameExist(AppKeyMixin, viewsets.ViewSet):

    def create(self, request):
        invalid = self.appkey_check(request.data)
        if invalid:
            return invalid

        try:
            Member.objects.get(username=request.data['username'])
        except Member.DoesNotExist:
            return Response({'code': '1', 'message': 'username is available'})

        return Response({'code': '0', 'message': 'username already exists!'})


class Login(AppKeyMixin, viewsets.ViewSet):
    
    def create(self, request):
        pass
        # invalid = self.appkey_check(request.data)
        # if invalid:
        #     return invalid

        # try:                                    
        #     member = Member.objects.get(username=request.data['username'])        
        # except Member.DoesNotExist:
        #     return Response({'code':'0', 'message':'username tidak ditemukan'})

        # if member.check_password(request.data['password']):
        #     token = MemberToken.create_token(member)
        #     return Response({'code':'1', 'message':token})
        # else:
        #     return Response({'code':'0', 'message':{'pass':member.password, 
        #                     'mess': member.check_password(request.data['password'])}})

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

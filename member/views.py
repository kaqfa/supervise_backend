"""View untuk handling request student dan supervisor"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route, list_route
from app.models import Application
from app.views import AppKeyMixin, app_key_required
from .serializers import RegisterSerializer, ProfileSerializer
from .serializers import UserSerializer, ProposalSerializer, ExpertiseSerializer
from progress.serializers import StudentProgressSerializer, TaskSerializer
from progress.serializers import StudentTaskSerializer
from member.models import Member, User, StudentProposal, Expertise
from progress.models import StudentTask, Template, Task
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class UserViewsets(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


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

    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'update':
            return RegisterSerializer
        return ProfileSerializer

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

    @detail_route(methods=['put'])
    def claim(self, request, pk):
        student = Member.objects.get(pk=pk)
        student.status = 'g'
        student.save()
        if request.data['files'] != None:
            print('print upload files')
        student = ProfileSerializer(student, context={'request':request})
        return Response(student.data)


class SupervisorViewsets(viewsets.ModelViewSet):
    queryset = Member.objects.filter(level='sp')
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    @list_route(methods=['get'])
    def get_student_progress(self, request):
        supervisor = Member.objects.get(user=self.request.user)
        students = Member.objects.filter(supervisor=supervisor)
        progress = []
        for data in students:
            progress.append(data.get_progress_data())
        # serial = StudentProgressSerializer(progress)
        return Response(progress)

    @list_route(methods=['post'])
    def response(self, request):
        username = request.data['username']
        student = Member.objects.get(user__username=username)
        prop = StudentProposal.objects.get(student=student, supervisor__user=request.user)
        prop.response(request.data['code'])
        return Response({'code': '1'})

    @detail_route(methods=['get'])
    def graduated(self, request, pk):
        graduated = Member.objects.filter(supervisor=pk, status='g')
        students = ProfileSerializer(graduated, many=True, context={'request': request})
        return Response(students.data)

    @detail_route(methods=['get'])
    def ungraduated(self, request, pk):
        graduated = Member.objects.filter(supervisor=pk, status='a')
        students = ProfileSerializer(graduated, many=True, context={'request': request})
        return Response(students.data)


class ExpertiseViewsets(viewsets.ModelViewSet):
    queryset = Expertise.objects.all()
    serializer_class = ExpertiseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['name', 'description']
    search_fields = ['name', 'description']

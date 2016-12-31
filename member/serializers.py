from rest_framework import serializers
from app.models import Application
from .models import Member, StudentProposal, Expertise
from rest_framework import status
from django.contrib.auth.models import User


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    nim = serializers.CharField(max_length=20, required=False)
    npp = serializers.CharField(max_length=20, required=False)
    address = serializers.CharField(required=False, allow_blank=True)
    phone = serializers.CharField(required=False, allow_blank=True)
    level = serializers.CharField(max_length=2)

    def validate(self, attrs):
        if attrs.get('nim') is None and attrs.get('level') == 'st':
            raise serializers.ValidationError("Mahasiswa harus memiliki NIM",
                                              status.HTTP_400_BAD_REQUEST)
        elif attrs.get('npp') is None and attrs.get('level') == 'sp':
            raise serializers.ValidationError("Pembimbing harus memiliki NPP",
                                              status.HTTP_400_BAD_REQUEST)
        else:
            return attrs

    def create(self, validated_data):
        userdata = {'username':validated_data.get('username'),
                    'password':validated_data.get('password'),
                    'first_name':validated_data.get('name'),
                    'last_name':validated_data.get('name'),
                    'email':validated_data.get('email')}
        user = User(**userdata)
        user.save()
        memberdata = {'user':user, 'npp':validated_data.get('npp', None),
                      'nim': validated_data.get('nim', None),
                      'address':validated_data.get('address', None),
                      'phone':validated_data.get('phone', None),
                      'level':validated_data.get('level')}
        return Member.objects.create(**memberdata)    



class ExpertiseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expertise
        fields = ('name', 'description')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Member
        fields = ('user', 'nim', 'npp', 'address', 'phone', 'status')


class ProposalSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentProposal
        fields = ('student', 'supervisor', 'status', 'propose_date', 'response_data')

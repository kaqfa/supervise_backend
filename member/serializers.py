from rest_framework import serializers
from app.models import Application
from .models import Member
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

    # class Meta:
    #     model = Member
    #     fields = ('username', 'password', 'nim', 'npp', 'name', 'address',
    #               'phone', 'email', 'level')

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


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Member
        fields = ('user', 'nim', 'npp', 'address', 'phone')

    # def update(self, instance, validated_data):
    #     instance.nim = validated_data.get('nim', instance.nim)
    #     instance.npp = validated_data.get('npp', instance.npp)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.level = validated_data.get('level', instance.level)

    #     return instance
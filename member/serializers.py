from rest_framework import serializers
from app.models import Application
from .models import Member
from rest_framework import status


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('username', 'password', 'nim', 'npp', 'name', 'address',
                  'phone', 'email', 'level')

    def validate(self, attrs):
        if attrs.get('nim') is None and attrs.get('level') == 'st':
            raise serializers.ValidationError("Mahasiswa harus memiliki NIM", status.HTTP_400_BAD_REQUEST)
        elif attrs.get('npp') is None and attrs.get('level') == 'sp':
            raise serializers.ValidationError("Pembimbing harus memiliki NPP", status.HTTP_400_BAD_REQUEST)
        else:
            return attrs

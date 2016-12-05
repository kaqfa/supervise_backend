from rest_framework import serializers
from app.models import Application
from .models import Member

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('username', 'password', 'nim', 'npp', 'name', 'address',
                  'phone', 'email', 'level')

    def validate(self, attrs):
        if attrs.get('nim') is None and attrs.get('level') == 'st':
            raise serializers.ValidationError("Pendaftaran mahasiswa harus menggunakan NIM")
        elif attrs.get('npp') is None and attrs.get('level') == 'sp':
            raise serializers.ValidationError("Pendaftaran pembimbing harus menggunakan NPP")
        else:
            return attrs

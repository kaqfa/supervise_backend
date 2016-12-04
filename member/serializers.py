from rest_framework import serializers
from app.models import Application
from .models import Member

class RegisterSerializer(serializers.ModelSerializer):
    # nim = serializers.CharField(max_length=20, allow_null=True)
    # npp = serializers.CharField(max_length=20, allow_null=True)
    class Meta:
        model= Member
        fields = ('username', 'password', 'nim', 'npp', 'name', 'address', 'phone', 'email', 'level')


    def validate(self, attrs):
        if attrs.get('nim') is None and attrs.get('level') == 's':
            raise serializers.ValidationError("Pendaftaran mahasiswa harus menggunakan NIM")
        elif attrs.get('npp') is None and attrs.get('level') == 'sp':
            raise serializers.ValidationError("Pendaftaran pembimbing harus menggunakan NPP")
        else:
            return attrs
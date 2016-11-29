from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    """*appkey, *username, *password, *nim, *name, address, handphone, email"""
    appkey = serializers.CharField(max_length=20)
    # username = serializers.CharField(min_length=4, max_length=20)
    # password = serializers.CharField(min_length=5, max_length=30)
    # nim = serializers.CharField(max_length=20, allow_null=True)
    # npp = serializers.CharField(max_length=20, allow_null=True)
    # name = serializers.CharField(max_length=50)
    # address = serializers.CharField(max_length=255, allow_null=True)
    # handphone = serializers.CharField(max_length=25, allow_null=True)
    # email = serializers.EmailField()

    class Meta:
        model: Member
        fields = (username, password, nim, npp, name, address, phone, email)
            
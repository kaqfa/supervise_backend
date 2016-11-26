from rest_framework import serializers


class FooSerializer(serializers.Serializer):
    code = serializers.CharField(required=False, max_length=1)
    message = serializers.CharField(required=False, max_length=200)
    data = serializers.CharField(required=False, max_length=200)


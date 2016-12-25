from rest_framework import serializers
from .models import Thesis, Task, Template


class ThesisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thesis
        fields = ('topic', 'title', 'abstract', 'student',
                  'field', 'files', 'save_date')

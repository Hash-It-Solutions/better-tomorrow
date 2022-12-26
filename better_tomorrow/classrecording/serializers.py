from rest_framework import serializers
from .models import ClassRecording

class ClassRecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassRecording
        fields='__all__'
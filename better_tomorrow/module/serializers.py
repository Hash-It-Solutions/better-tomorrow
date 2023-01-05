from rest_framework import serializers
from .models import Module
from course.serializers import CourseSerializer
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Module
        fields='__all__'
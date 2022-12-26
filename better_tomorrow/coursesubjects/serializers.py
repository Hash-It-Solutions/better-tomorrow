from rest_framework import serializers
from .models import CourseSubjects

class CourseSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseSubjects
        fields='__all__'
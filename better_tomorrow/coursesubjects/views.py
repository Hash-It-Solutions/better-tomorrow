from django.shortcuts import render
from .models import CourseSubjects
from rest_framework import viewsets
from .serializers import CourseSubjectsSerializer
# Create your views here.
class CourseSubjectsViewset(viewsets.ModelViewSet):
    serializer_class=CourseSubjectsSerializer
    queryset=CourseSubjects.objects.all()
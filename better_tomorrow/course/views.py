from django.shortcuts import render
from .models import Course
from rest_framework import viewsets
from .serializers import CourseSerializer
# Create your views here.
class CourseViewset(viewsets.ModelViewSet):
    serializer_class=CourseSerializer
    queryset=Course.objects.all()

def CourseListing(request):
    return render(request,'Course/CourseListing.html')

def CourseDetails(request):
    return render(request,'Course/CourseDetails.html')
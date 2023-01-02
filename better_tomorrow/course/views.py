from django.shortcuts import render
from .models import Course
from rest_framework import viewsets
from .serializers import CourseSerializer
import requests
# Create your views here.
class CourseViewset(viewsets.ModelViewSet):
    serializer_class=CourseSerializer
    queryset=Course.objects.all()

# def CourseListing(request):
#     return render(request,'Course/CourseListing.html')

def CourseDetails(request):
    return render(request,'Course/CourseDetails.html')

def CourseListing(request):
    response=requests.get('http://localhost:8000/api/CourseApi/CourseApi/').json()
    return render(request,'Course/CourseListing.html',{'response':response})
from django.shortcuts import render
from .serializers import SubjectSerializer
from rest_framework import viewsets
from .models import Subject
# Create your views here.


class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

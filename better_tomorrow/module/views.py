from django.shortcuts import render
from .serializers import ModuleSerializer
from .models import Module
from rest_framework import viewsets
# Create your views here.
class ModuleViewSet(viewsets.ModelViewSet):
    serializer_class=ModuleSerializer
    queryset=Module.objects.all()
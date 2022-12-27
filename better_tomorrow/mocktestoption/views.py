from django.shortcuts import render
from .serializers import MocktestOptionSerializer
from rest_framework import viewsets
from .models import MockTestOption
# Create your views here.

class MocktestOptionViewset(viewsets.ModelViewSet):
    serializer_class=MocktestOptionSerializer
    queryset=MockTestOption.objects.all()
from django.shortcuts import render
from .models import Mocktest
from rest_framework import viewsets
from .serializers import MocktestSerializer
import requests
# Create your views here.
class MocktestViewset(viewsets.ModelViewSet):
    serializer_class=MocktestSerializer
    queryset=Mocktest.objects.all()




def MockTestQuestion(request):
    MockTestQuestion = requests.get('http://localhost:8000/api/MockTestQuestionApi/MockTestQuestionApi/').json()
    MockTestOption=requests.get('http://localhost:8000/api/MocktestOptionApi/MocktestOptionApi/').json()
    return render(request, 'MockTest/MockTest.html', {'MockTestQuestion': MockTestQuestion,'MockTestOption':MockTestOption})
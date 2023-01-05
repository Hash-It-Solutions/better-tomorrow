from django.shortcuts import render
from .serializers import MockTestQuestionSerializer
from rest_framework import viewsets
from .models import MockTestQuestion
import requests
# Create your views here.


class MockTestQuestionviewset(viewsets.ModelViewSet):
    serializer_class = MockTestQuestionSerializer
    queryset = MockTestQuestion.objects.all()


def MockTestQuestion(request):
    MockTestQuestion = requests.get('http://localhost:8000/api/MockTestQuestionApi/MockTestQuestionApi/').json()
    MockTestOption=requests.get('http://localhost:8000/api/MocktestOptionApi/MocktestOptionApi/').json()
    return render(request, 'MockTest/MockTest.html', {'MockTestQuestion': MockTestQuestion,'MockTestOption':MockTestOption})

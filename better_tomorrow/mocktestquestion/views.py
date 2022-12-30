from django.shortcuts import render
from .serializers import MockTestQuestionSerializer
from rest_framework import viewsets
from .models import MockTestQuestion
import requests
# Create your views here.


class MockTestQuestionviewset(viewsets.ModelViewSet):
    serializer_class=MockTestQuestionSerializer
    queryset=MockTestQuestion.objects.all()


def api(request):
    response=requests.get('http://localhost:8000/api/MockTestQuestionApi/MockTestQuestionApi/').json()
    print(response)
    return render(request,'Home/UserHome.html',{'response':response})

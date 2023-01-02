from django.shortcuts import render
from .serializers import MocktestOptionSerializer
from rest_framework import viewsets
from .models import MockTestOption
import requests
# Create your views here.
class MocktestOptionViewset(viewsets.ModelViewSet):
    serializer_class=MocktestOptionSerializer
    queryset=MockTestOption.objects.all()

def api(request):
    response=requests.get('http://localhost:8000/api/MocktestOptionApi/MocktestOptionApi/').json()
    return render(request,'Home/UserHome.html',{'response':response})
from django.shortcuts import render
from .models import Mocktest
from rest_framework import viewsets
from .serializers import MocktestSerializer
# Create your views here.
class MocktestViewset(viewsets.ModelViewSet):
    serializer_class=MocktestSerializer
    queryset=Mocktest.objects.all()

def MockTestDetails(request):
    return render(request,'MockTest/MockTestDetails.html')
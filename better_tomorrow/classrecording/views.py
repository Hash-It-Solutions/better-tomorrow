from django.shortcuts import render
from .models import ClassRecording
from rest_framework import viewsets
# Create your views here.

from .models import ClassRecording

from .serializers import ClassRecordingSerializer

class ClassRecordingViewset(viewsets.ModelViewSet):
    serializer_class=ClassRecordingSerializer
    queryset=ClassRecording.objects.all()
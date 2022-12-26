from django.shortcuts import render
from .models import ClassRecording
from rest_framework import viewsets
from .serializers import ClassRecordingSerializer
# Create your views here.
class ClassRecordingViewset(viewsets.ModelViewSet):
    serializer_class=ClassRecordingSerializer
    queryset=ClassRecording.objects.all()
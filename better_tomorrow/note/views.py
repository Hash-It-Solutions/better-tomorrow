from django.shortcuts import render
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer
# Create your views here.

class  NoteViewSet(viewsets.ModelViewSet):
    serializer_class=NoteSerializer
    queryset=Note.objects.all()
from django.shortcuts import render
from .serializers import MockTestQuestionSerializer
from rest_framework import viewsets
from .models import MockTestQuestion
# Create your views here.


class MockTestQuestionviewset(viewsets.ModelViewSet):
    serializer_class=MockTestQuestionSerializer
    queryset=MockTestQuestion.objects.all()
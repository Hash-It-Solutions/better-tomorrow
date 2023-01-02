from django.shortcuts import render
from .serializers import UserSubscriptionSerializer
from rest_framework import viewsets
from .models import UserSubscription
# Create your views here.
class UserSubscriptionViewset(viewsets.ModelViewSet):
    serializer_class=UserSubscriptionSerializer
    queryset=UserSubscription.objects.all()
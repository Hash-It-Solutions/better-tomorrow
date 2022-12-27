from django.shortcuts import render
from .serializers import SubscriptionSerializer
from rest_framework import viewsets
from .models import Subscription
# Create your views here.
class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class=SubscriptionSerializer
    queryset=Subscription.objects.all()
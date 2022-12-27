from rest_framework import serializers
from .models import Mocktest

class MocktestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mocktest
        fields='__all__'
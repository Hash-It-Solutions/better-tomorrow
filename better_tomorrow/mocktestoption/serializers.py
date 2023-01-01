from rest_framework import serializers
from .models import MockTestOption
class MocktestOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=MockTestOption
        fields='__all__'
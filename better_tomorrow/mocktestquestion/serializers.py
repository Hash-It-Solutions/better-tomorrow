from rest_framework import serializers
from .models import MockTestQuestion
class MockTestQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=MockTestQuestion
        fields='__all__'
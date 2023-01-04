from rest_framework import serializers
from .models import Module
class ModuleSerializer(serializers.ModelSerializer):
    course=serializers.RelatedField(source='Module',read_only=True)
    class Meta:
        model=Module
    # def to_representation(self, instance):
    #     representation = dict()
    #     representation["id"] = instance.id
    #     representation["course"] = instance.course
    #     representation["title"] = instance.title
    #     representation["description"] = instance.description
    #     return representation

        fields=('id','title','description','course')
        fields='__all__'
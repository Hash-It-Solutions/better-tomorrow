from django.db import models
from module.models import Module
# Create your models here.
class Note(models.Model):
    id=models.IntegerField(primary_key=True)
    module=models.ForeignKey(Module,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=100)
    
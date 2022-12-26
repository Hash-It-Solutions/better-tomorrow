from django.db import models

# Create your models here.
class Subject(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    
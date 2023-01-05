from django.db import models
from mocktestquestion.models import MockTestQuestion
# Create your models here.
class MockTestOption(models.Model):
    id=models.IntegerField(primary_key=True)
    question_id=models.ForeignKey(MockTestQuestion,on_delete=models.CASCADE)
    option=models.CharField(max_length=50)
    is_correct=models.BooleanField()

    
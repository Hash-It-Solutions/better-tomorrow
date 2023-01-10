from django.db import models
from subject.models import Subject
from mocktest.models import Mocktest
# Create your models here.
class MockTestQuestion(models.Model):
    id=models.IntegerField(primary_key=True)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    mock_test=models.ForeignKey(Mocktest,on_delete=models.CASCADE)
    question=models.TextField(max_length=500)

    def __str__(self):
        return self.question


    
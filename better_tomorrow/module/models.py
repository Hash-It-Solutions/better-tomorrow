from django.db import models
from course.models import Course
# Create your models here.
class Module(models.Model):
    id=models.IntegerField(primary_key=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=100)
    
    def __str__(self):
        return self.title
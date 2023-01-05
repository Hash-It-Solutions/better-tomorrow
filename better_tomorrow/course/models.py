from django.db import models
# Create your models here.
class Course(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50,)
    description=models.TextField(max_length=100)

    def __str__(self):
        return self.name
    
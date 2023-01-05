from django.db import models
# Create your models here.
class Subscription(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    duration=models.IntegerField()


    def __str__(self):
        return self.name


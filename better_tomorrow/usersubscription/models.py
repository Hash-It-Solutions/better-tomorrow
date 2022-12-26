from django.db import models
from user.models import User
from subscription.models import Subscription
# Create your models here.
class UserSubscription(models.Model):
    id=models.IntegerField(primary_key=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    subscripion_id=models.ForeignKey(Subscription,on_delete=models.CASCADE)
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateTimeField()
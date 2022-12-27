from django.urls import path,include
from rest_framework import routers
from .views import UserSubscriptionViewset
router=routers.DefaultRouter()
router.register(r'UserSubscripitonApi',UserSubscriptionViewset)

urlpatterns=[
    path('api/UserSubscriptionApi/',include(router.urls))
]
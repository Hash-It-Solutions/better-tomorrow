from django.urls import path,include
from .views import SubscriptionViewSet
from rest_framework import routers
router=routers.DefaultRouter()
from subscription import views
router.register(r'SubscriptionApi',SubscriptionViewSet)

urlpatterns=[
    path('api/SubscriptionApi/',include(router.urls)),
    path('SubscriptionDetails/',views.SubscriptionDetails,name='SubscriptionDetails'),
]
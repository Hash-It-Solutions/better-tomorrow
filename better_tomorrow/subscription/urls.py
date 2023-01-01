from subscription import views
from django.urls import path, include
from .views import SubscriptionViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'SubscriptionApi', SubscriptionViewSet)
urlpatterns = [
    path('api/SubscriptionApi/', include(router.urls)),
    path('SubscriptionDetails/', views.SubscriptionDetails,name='SubscriptionDetails'),
]

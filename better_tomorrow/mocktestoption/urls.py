from django.urls import path,include
from rest_framework import routers
from .views import MocktestOptionViewset
router=routers.DefaultRouter()
router.register(r'MocktestOptionApi',MocktestOptionViewset)

urlpatterns=[
    path('api/MocktestOptionApi/',include(router.urls))
]
from django.urls import path,include
from rest_framework import routers
from .views import MocktestViewset
router=routers.DefaultRouter()
router.register(r'Mocktest',MocktestViewset)
urlpatterns=[
    path('MocktestApi/',include(router.urls))

]
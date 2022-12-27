from django.urls import path,include
from .views import ModuleViewSet
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'ModuleApi',ModuleViewSet)
urlpatterns=[
    path('api/ModuleApi/',include(router.urls))
]
from django.urls import path,include
from .views import ModuleViewSet
from rest_framework import routers
router=routers.DefaultRouter()
from module import views
router.register(r'ModuleApi',ModuleViewSet)
urlpatterns=[
    path('api/ModuleApi/',include(router.urls)),
    path('ModuleDetails/',views.ModuleDetails,name='ModuleDetails'),
]
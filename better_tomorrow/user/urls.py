from django.urls import path,include
from rest_framework import routers
from .views import UserViewSet
router=routers.DefaultRouter()
router.register(r'UserApi',UserViewSet)
urlpatterns=[
    path('api/UserApi/',include(router.urls))

]
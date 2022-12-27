from django.urls import path,include
from rest_framework import routers
from .views import UserViewSet
from  user import views
router=routers.DefaultRouter()
router.register(r'UserApi',UserViewSet)
urlpatterns=[
    path('api/UserApi/',include(router.urls)),
    path('signup/',views.signup,name='signup')
]
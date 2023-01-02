from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet
from user import views
router = routers.DefaultRouter()
router.register(r'UserApi', UserViewSet)
urlpatterns = [
    path('api/UserApi/', include(router.urls)),
    path('SignUp/', views.SignUp, name='SignUp'),
    path('SignIn/', views.SignIn, name='SignIn'),
    path('UserHome/', views.UserHome, name='UserHome'),
    path('LogOut/', views.LogOut, name='LogOut'),
]

from django.urls import path, include
from .views import MockTestQuestionviewset
from rest_framework import routers
from mocktestquestion import views
router = routers.DefaultRouter()
router.register(r'MockTestQuestionApi', MockTestQuestionviewset)
urlpatterns = [
    path('api/MockTestQuestionApi/', include(router.urls)),
    path('MockTestQuestion/', views.MockTestQuestion, name='MockTestQuestion'),
]

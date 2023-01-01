from django.urls import path, include
from .views import NoteViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'NoteApi', NoteViewSet)
urlpatterns = [
    path('api/NoteApi/', include(router.urls))
]

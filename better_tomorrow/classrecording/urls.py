from django.urls import path,include
from .views import ClassRecordingViewset
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'ClassRecordingApi',ClassRecordingViewset)
urlpatterns =[
    path('api/ClassRecordingApi/',include(router.urls)),
    
]
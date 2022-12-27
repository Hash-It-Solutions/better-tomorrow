from django.urls import path,include
from .views import SubjectViewSet
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'SubjectApi',SubjectViewSet)
urlpatterns=[
    path('api/SubjectApi/',include(router.urls))
]
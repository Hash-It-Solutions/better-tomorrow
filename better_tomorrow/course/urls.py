from django.urls import path,include
from .views import CourseViewset
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'Course',CourseViewset)
urlpatterns=[
    path('CourseApi',include(router.urls)),
]
from django.urls import path,include
from .views import CourseSubjectsViewset
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'CourseSubjectsApi',CourseSubjectsViewset)
urlpatterns=[
    path('api/CourseSubjectsApi/',include(router.urls))
]

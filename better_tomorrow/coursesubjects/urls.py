from django.urls import path,include
from .views import CourseSubjectsViewset
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'CourseSubjects',CourseSubjectsViewset)
urlpatterns=[
    path('CourseSubjectsApi',include(router.urls))
]

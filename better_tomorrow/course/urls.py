from django.urls import path,include
from .views import CourseViewset
from course import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'CourseApi',CourseViewset)
urlpatterns=[
    path('api/CourseApi/',include(router.urls)),
    path('CourseListing/',views.CourseListing,name='CourseListing'),
    path('CourseDetails/',views.CourseDetails,name='CourseDetails'),
]
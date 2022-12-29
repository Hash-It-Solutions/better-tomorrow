from django.urls import path,include
from rest_framework import routers
from .views import MocktestViewset
from mocktest import views
router=routers.DefaultRouter()
router.register(r'MocktestApi',MocktestViewset)
urlpatterns=[
    path('api/MocktestApi/',include(router.urls)),
    path('MockTestDetails/',views.MockTestDetails,name='MockTestDetails'),

]
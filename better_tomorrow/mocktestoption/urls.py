from django.urls import path,include
from rest_framework import routers
from .views import MocktestOptionViewset
from mocktestoption import views
router=routers.DefaultRouter()
router.register(r'MocktestOptionApi',MocktestOptionViewset)

urlpatterns=[
    path('api/MocktestOptionApi/',include(router.urls)), 
    path('apitestoption/',views.api,name='api'),

]
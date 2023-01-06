from django.urls import path, include
from custom_admin import views
urlpatterns = [
   path('customadmin/',views.Custom_Admin,name='Custom_Admin'),
]

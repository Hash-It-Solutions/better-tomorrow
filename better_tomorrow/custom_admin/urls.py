from django.urls import path, include
from custom_admin import views
urlpatterns = [
   path('customadmin/',views.Custom_Admin_Login,name='Custom_Admin'),
   path('customadmin_dashboard/',views.Custom_Admin_Dashboard,name='Custom_Admin_Dashboard'),
]

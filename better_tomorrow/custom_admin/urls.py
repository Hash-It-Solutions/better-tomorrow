from django.urls import path, include
from custom_admin import views
urlpatterns = [
   path('customadmin/',views.Custom_Admin_Login,name='Custom_Admin'),
   path('customadmin_home/',views.Custom_Admin_Home,name='Custom_Admin_Home'),
   path('customadmin_dashbord/',views.Custom_Admin_Dashboard,name='Custom_Admin_Dashboard'),
   path('Course_admin_add/',views.Course_admin_add,name='Course_admin_add'),
   path('Course_admin_View/',views.Course_admin_View,name='Course_admin_View'),
]

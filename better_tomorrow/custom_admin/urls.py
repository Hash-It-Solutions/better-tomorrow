from django.urls import path, include
from custom_admin import views
urlpatterns = [
   path('customadmin/',views.Custom_Admin_Login,name='Custom_Admin'),
   path('customadmin_home/',views.Custom_Admin_Home,name='Custom_Admin_Home'),
   path('customadmin_dashbord/',views.Custom_Admin_Dashboard,name='Custom_Admin_Dashboard'),

   path('Course_admin_add/',views.Course_admin_Add,name='Course_admin_Add'),
   path('Course_admin_View/',views.Course_admin_View,name='Course_admin_View'),
   path('Course_admin_Delete/<int:id>',views.Course_admin_Delete,name='Course_admin_Delete'),
   path('Course_admin_Update/<int:id1>',views.Course_admin_Update,name='Course_admin_Update'),

   path('Mocktest_admin_Add/',views.Mocktest_admin_Add,name='Mocktest_admin_Add'),
   path('Mocktest_admin_View/',views.Mocktest_admin_View,name='Mocktest_admin_View'),
   path('Mocktest_admin_Delete/<int:id>',views.Mocktest_admin_Delete,name='Mocktest_admin_Delete'),
   path('Mocktest_admin_Update/<int:id1>',views.Mocktest_admin_Update,name='Mocktest_admin_Update'),

   path('Module_admin_Add/',views.Module_admin_Add,name='Module_admin_Add'),
   path('Module_admin_View/',views.Module_admin_View,name='Module_admin_View'),
   path('Module_admin_Delete/<int:id>',views.Module_admin_Delete,name='Module_admin_Delete'),
   path('Module_admin_Update/<int:id1>',views.Module_admin_Update,name='Module_admin_Update'),


   
   path('Note_admin_Add/',views.Note_admin_Add,name='Note_admin_Add'),
   path('Note_admin_View/',views.Note_admin_View,name='Note_admin_View'),
   path('Note_admin_Update/<int:id1>',views.Note_admin_Update,name='Note_admin_Update'),
   path('Note_admin_Delete/<int:id>',views.Note_admin_Delete,name='Note_admin_Delete'),


    path('Mocktest_Question_Add/',views.Mocktest_Question_Add,name='Mocktest_Question_Add'),
    path('Mocktest_Question_View/',views.Mocktest_Question_View,name='Mocktest_Question_View'),
   

]

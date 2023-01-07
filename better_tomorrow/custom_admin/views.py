from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from course.models import Course
# Create your views here.

def Custom_Admin_Login(request):  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('Custom_Admin_Home')
        else:
            return HttpResponse('username or password is not correct')
    return render(request,'CustomAdmin/login.html')

     

def Custom_Admin_Home(request):
     return render(request,'CustomAdmin/index.html')


def Custom_Admin_Dashboard(request):
    return render(request,'CustomAdmin/dashboard.html')
    

def Course_admin_add(request):
    if request.method == 'POST':
        id = request.POST.get('course_id')
        name = request.POST.get('course_name')
        description = request.POST.get('course_description')
        obj=Course(id=id,name=name,description=description)
        obj.save()
        return HttpResponse('course added successfully')
    return render(request,'CustomAdmin/Add_Courses.html')


def Course_admin_View(request):
    objs=Course.objects.all()
    return render(request,'CustomAdmin/View_Courses.html',{'objs':objs})

# def Custom_Admin_Login(request):     
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user=User.objects.filter(username=username)
#             if not user.exists():
#                  messages.info(request,'Account Not Found')
#                  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#             user = authenticate(request, username=username, password=password)
#             if user and user.is_superuser:
#                 login(request,user)
#                 return redirect('Custom_Admin_Dashboard')
#             else:
#                 messages.info(request,'Invalid Password')
#                 return redirect('/')
#         return render(request, 'CustomAdmin/login.html')
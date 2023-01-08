from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from course.models import Course
from mocktest.models import Mocktest
from module.models import Module
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



                       # admin side of course

def Course_admin_Add(request):
    if request.method == 'POST':
        id = request.POST.get('course_id')
        name = request.POST.get('course_name')
        description = request.POST.get('course_description')
        obj=Course(id=id,name=name,description=description)
        obj.save()
        return redirect('Course_admin_View')
    return render(request,'CustomAdmin/Add_Courses.html')


def Course_admin_View(request):
    objs=Course.objects.all()
    return render(request,'CustomAdmin/View_Courses.html',{'objs':objs})


def Course_admin_Delete(request,id):
    obj=Course.objects.get(pk=id)
    obj.delete()
    return redirect('Course_admin_View')


def Course_admin_Update(request,id1):
    if request.method == 'POST':
        id = request.POST.get('course_id')
        name = request.POST.get('course_name')
        description = request.POST.get('course_description')
        Course.objects.filter(pk=id1).update(id=id,name=name,description=description)
        return redirect('Course_admin_View')
    else:
        obj=Course.objects.get(pk=id1)
        return render(request,'CustomAdmin/Edit_Courses.html',{'obj':obj})



            #   admin side of Mocktest

def Mocktest_admin_Add(request):
    if request.method == 'POST':
        id = request.POST.get('mocktest_id')
        module_id = request.POST.get('module')
        module=Module.objects.get(id=module_id)
        mocktest_title = request.POST.get('mocktest_title')
        description = request.POST.get('mocktest_description')
        date = request.POST.get('mocktest_date')
        obj=Mocktest(id=id,module=module,title=mocktest_title,description=description,due_date=date)
        obj.save()
        return redirect('Mocktest_admin_View')
    else:
        module=Module.objects.all()
        return render(request,'CustomAdmin/Add_Mocktest.html',{'module':module})


def Mocktest_admin_View(request):
    module=Mocktest.objects.all()
    return render(request,'CustomAdmin/View_Mocktest.html',{'module':module})

def Mocktest_admin_Delete(request,id):
    module=Mocktest.objects.get(pk=id)
    module.delete()
    return redirect('Mocktest_admin_View')

def Mocktest_admin_Update(request,id1):
    if request.method == 'POST':
        id = request.POST.get('mocktest_id')
        module_id = request.POST.get('module')
        module=Module.objects.get(id=module_id)
        mocktest_title = request.POST.get('mocktest_title')
        description = request.POST.get('mocktest_description')
        date = request.POST.get('date')
        Mocktest.objects.filter(pk=id1).update(id=id,module=module,mocktest_title=mocktest_title,description=description,due_date=date)
        return redirect('Mocktest_admin_View')
    else:
        module=Mocktest.objects.get(pk=id1)
        return render(request,'CustomAdmin/Edit_Mocktest.html',{'module':module})

            #    admin side of module
def Module_admin_Add(request):
    if request.method == 'POST':
        id = request.POST.get('module_id')
        course_id = request.POST.get('course')
        course=Course.objects.get(id=course_id)
        module_title = request.POST.get('module_title')
        module_description = request.POST.get('module_description')
        obj=Module(id=id,course=course,title=module_title,description=module_description)
        obj.save()
        return redirect('Module_admin_View')
    else:
        objs=Course.objects.all()
        return render(request,'CustomAdmin/Add_Module.html',{'objs':objs})

def Module_admin_View(request):
    objs=Module.objects.all()
    return render(request,'CustomAdmin/View_Module.html',{'objs':objs})


def Module_admin_Delete(request,id):
    module=Module.objects.get(pk=id)
    module.delete()
    return redirect('Module_admin_View')



def Module_admin_Update(request,id1):
    if request.method == 'POST':
        id = request.POST.get('module_id')
        course_id = request.POST.get('course')
        course=Course.objects.get(id=course_id)
        module_title = request.POST.get('module_title')
        module_description = request.POST.get('module_description')
        Module.objects.filter(pk=id1).update(id=id,course=course,title=module_title,description=module_description)
        return redirect('Module_admin_View')
    else:
        objs=Module.objects.get(pk=id1)
        return render(request,'CustomAdmin/Edit_Module.html',{'objs':objs})











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
from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def Custom_Admin_Login(request):  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('Custom_Admin_Dashboard')
        else:
            return HttpResponse('username or password is not correct')
    return render(request,'CustomAdmin/login.html')

     

def Custom_Admin_Dashboard(request):
     return render(request,'CustomAdmin/index.html')
    


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
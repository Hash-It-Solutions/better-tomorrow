from django.shortcuts import render,HttpResponse
from .serializers import UserSerializer
from .models import User
from rest_framework import viewsets
from django.contrib.auth.models import User
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()


def signup(request):
    if request.method=='POST':
        fname=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        uname=request.POST.get('username')
        email=request.POST.get('email')
        number=request.POST.get('phone_number')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        user=User.objects.create_user(uname,email,password1)
        user.save()
        return HttpResponse('user created successfully')
        
    return render(request,'signup/signup.html')
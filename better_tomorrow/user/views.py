from django.shortcuts import render, HttpResponse, redirect
from .serializers import UserSerializer
from .models import User
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


def UserHome(request):
    return render(request, 'Home/UserHome.html')


def SignUp(request):
    if request.method == 'POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        number = request.POST.get('phone_number')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return HttpResponse('password and confirm password are not same')
        else:
            user = User.objects.create_user(uname, email, password1)
            user.save()
            return redirect('SignIn')
    return render(request, 'Signup/SignUp.html')


def SignIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=password1)
        if user != None:
            login(request, user)
            return redirect('UserHome')
        else:
            return HttpResponse('username or password is not correct')
    return render(request, 'SignIn/SignIn.html')


def LogOut(request):
    logout(request)
    return redirect('home')

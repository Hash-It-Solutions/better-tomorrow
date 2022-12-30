from django.shortcuts import render

def home(request):
    return render(request,'Index.html')


def About(request):
    return render(request,'About/about-us.html')

def Service(request):
    return render(request,'Service/service.html')

def Contact(request):
    return render(request,'Contact/contact-us.html')
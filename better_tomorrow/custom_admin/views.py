from django.shortcuts import render

# Create your views here.
def Custom_Admin(request):
    return render(request,'CustomAdmin/index.html')
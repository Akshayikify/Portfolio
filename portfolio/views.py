from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from . models import Projects
def home(request):
    projects=Projects.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        
        send_mail(
            f"Message from {name}",
            message,
            email,
            ['sumams758@gmail.com']
        )
    return render(request,'index.html',{'projects':projects})
        

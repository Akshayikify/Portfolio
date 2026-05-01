from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from . models import Projects
from django.core.mail import EmailMessage
from django.conf import settings
import os 
from dotenv import load_dotenv
load_dotenv()
def home(request):
    projects=Projects.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        
        mail = EmailMessage(
            subject=f"Message from {name}",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[os.getenv('EMAIL_HOST_USER')],
            reply_to=[email], 
        )
        mail.send()
    return render(request,'index.html',{'projects':projects})
        

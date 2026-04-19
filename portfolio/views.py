from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
def sign_up(request):
    pass
def login_user(request):
    pass
def home(request):
    context={'name':'Akshay'}
    return render(request,'index.html',context)
        

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from core.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# from django.utils import timezone
# Create your views here.

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
           login(request,user)
           return redirect('/')
        messages.info(request,"login failed Try again")
    return render(request,"accounts/login.html")

def user_register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        phone_field=request.POST.get('phone_field')

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                print("username already exits")
                return redirect('user_register')
            else:
                if User.objects.filter(email=email).exists():
                    print("email already exits")
                    return redirect('user_register')
                else:
                    user=User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    data=customer(user=user,phone_field=phone_field)
                    data.save()
                    our_user=authenticate(username=username,password=password)
                    if our_user is not None:
                        login(request,user)
                        return redirect('/')
        
        else:
           messages.info(request,"Registration is Failed try again")
           print("error")
           return redirect('user_register')
    return render(request,"accounts/register.html")

def user_logout(request):
    logout(request)
    return redirect('/')


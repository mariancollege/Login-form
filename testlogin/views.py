from django.shortcuts import render, render_to_response, redirect
from .models import *
from django.contrib import messages


# Create your views here.
def log(request):
    if request.method=="POST":
        un=request.POST["u"]
        ps=request.POST["p"]

        if logclass.objects.all().filter(uname=un).filter(pswd1=ps).exists():
            return redirect('/welcome',{'msg':'Successfully login'})
        else:
            return render(request, 'log.html',{'msg':'Incorrect username or password'})
    return render(request,'log.html')


def regis(request):
    if request.method=="POST":
        uuname=request.POST.get("name")
        ppswd1=request.POST.get("pswda")
        ppswd2=request.POST.get("pswdb")

        if ppswd1==ppswd2:
            if logclass.objects.all().filter(uname=uuname).exists():
                return render(request,'registration.html',{'e':'User already exists'})
            else:
                logclass.objects.get_or_create(uname=uuname,pswd1=ppswd1,pswd2=ppswd2)
                return redirect('/log',{'e':'Successfuly registered'})
        else:
            return render(request,'registration.html',{'e':'Password mismatch'})

    return render(request, 'registration.html')
def welcome(request):
    return render(request, 'welcome.html')
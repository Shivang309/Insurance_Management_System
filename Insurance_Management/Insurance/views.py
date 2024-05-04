from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def home_page(request):
    return render(request,'home_page.html')

def Customer_home(request):
    return render(request,'Customer_home.html')

def Customer_login(request):
    error=""
    if request.method=='POST':
        u = request.POST['emailid']
        p = request.POST['password']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            error="no"
        else:
            error="yes"
    return render(request,'Customer_login.html',locals())

def registration(request):
    error=""
    if request.method=="POST":
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        pn=request.POST['Phone_number']
        lc=request.POST['Address']
        em=request.POST['email']
        pwd=request.POST['pwd']
        try:
            user=User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            CustomerDetail.objects.create(user=user,Phone_number=pn,Address=lc)
            error="no"
        except:
            error="yes"

    return render(request,'registration.html',locals())

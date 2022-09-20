import imp
from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import UserInfo

# Create your views here.
def home(request):
    return render(request, "Organization/home.html")

def user_registration(request):
    if request.method == "POST":
        username = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request,"Your Account Has Been Succesfully Created")

        userInfo = UserInfo(Username=username, First_name=fname, Last_Name=lname, Email=email)
        userInfo.save()


        return redirect("home")






    return render(request,"Organization/register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return render(request, "Organization/dashboard/dashboard.html")

        else:
            messages.error(request, "Bad Credentials")
            return redirect("home")
    return render(request,"Organization/login.html")

def logOut(request):
    logout(request)
    return redirect("home")

def dashboard(request, username):
    if Username:
        uname = UserInfo.objects.get(Username=username)

    return render(request,"Organization/dashboard/dashboard.html")
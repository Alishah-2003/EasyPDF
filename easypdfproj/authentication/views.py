from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'authentication/home.html')

def signup(request):
    if request.method=="POST":
        first_name=request.POST["fname"]
        last_name=request.POST["lname"]
        email=request.POST["email"]
        password=request.POST["password"]

        if User.objects.filter(username=email).exists():
            return render(request, "authentication/signup.html", {
                "error": "A user with this email already exists, please login instead."
            })
        u=User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=email,
            email=email,
            password=password,
        )
        login(request,u)
        return redirect("/uploadfile/")
    else:
        return render(request,"authentication/signup.html")
    
def login_user(request):
    if request.method=="POST":
        
        email=request.POST["email"]
        password=request.POST["password"]

        user=authenticate(username=email, password=password)

        if user is not None:
            login(request,user)
            return redirect("/uploadfile/")
        else:
            return render(request,"authentication/login.html",{
                "error":"No such user exists, please sign up first."
            })
    return render(request,"authentication/login.html")

def logout_user(request):
    logout(request)
    return redirect("/")

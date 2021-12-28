from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout,login

# Create your views here.
def index(request):
    if request.user.is_authenticated:
    # Do something for authenticated users.
        return redirect("/")
    else:
    # Do something for anonymous users.
        return redirect("/login")
    
    
    

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
            return redirect('/')   
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return render(request, 'login.html')
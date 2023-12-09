from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, (f'{user.username} logged in'))
            return(redirect('map'))
            #Redirect to a success page.
        else:
            messages.success(request, ("There was an error logging in, try again...."))
            return(render(request,'authenticate/login.html'))

    else:
        return render(request, 'authenticate/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, ("Logout successful"))
    return(redirect('map'))

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from app.models import profile as profile_model
# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, (f'{user.username} logged in'))
            return(redirect('/'))
            #Redirect to a success page.
        else:
            messages.success(request, ("There was an error logging in, try again...."))
            return(render(request,'authenticate/login.html'))

    else:
        return render(request, 'authenticate/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, ("Logout successful"))
    return(redirect('/'))

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            profile_model.objects.create(userName=username, first='', last='', email='')
            login(request, user)
            messages.success(request, 'Account created!')
            return redirect('/')
    else:
        form = UserCreationForm()
    return(render(request,'authenticate/register.html', {'form': form}))

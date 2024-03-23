from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home (request):
    return render(request, 'home.html', {})


def login_user(request):
    #Check to see if logging in

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

    #Authenticate     
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login success!")
            return redirect('home')
        else:
            messages.success(request, "Error while Logging in")
            return redirect('login')

        
    
    return render(request, 'login.html', {})
    
    
    

def logout_user(request):
    logout(request)
    messages.success(request, "You've been logged out!")
    return render(request, 'home.html')

def register_user(request):
    return render(request, 'register.html', {})


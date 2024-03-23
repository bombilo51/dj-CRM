from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
from django.core.exceptions import ObjectDoesNotExist


def home (request):
    records = Record.objects.all()

    return render(request, 'home.html', {'records':records})


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
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You've been successfully registered!")
            return  redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):

    if not request.user.is_authenticated:
        messages.success(request, "You must be logged in to view this page!")
        return redirect('home')

    try:
        record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'record':record})
    except ObjectDoesNotExist as e:
        messages.success(request, f"Object with id: {pk} doesn't exist!")
        return redirect('home')
    except Exception as e:
        messages.success(request, "Unknown exception:" + e.__str__)
        return redirect('home') 

def delete_customer_record(request, pk):
    try:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, f"Object {record} with id: {pk} Deleted")
    except ObjectDoesNotExist as e:
        messages.success(request, f"Object with id: {pk} doesn't exist!")
    except Exception as e:
        messages.success(request, e)

    return redirect('home')

def create_record(request):
    messages.success(request, f"Not implemented yet! (create_record)")

    if request.method == 'POST':
        create_record_post()

    return redirect('home')

def create_record_post(request):
    return redirect('home')

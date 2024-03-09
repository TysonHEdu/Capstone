from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/admin/') # Redirect to a success page. just the django admin page for now CHANGE THIS SHIT LATER
        else:
            messages.warning(request, ("There was an error logging in, please try again..."))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html')

#DO SOME LOGOUT FUNCTION ONCE A BAST PAGE IS CREATED

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration success!"))
            return redirect('/admin/') #change this again once we have something setup
    else:
        form = UserCreationForm()

    return render(request, 'authenticate/register.html', {
        'form':form,
        })

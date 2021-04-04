from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import CreateUserForm, AddPhoneNumberForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# from test import u
# Create your views here.

def join(request):

    if request.user.is_authenticated:
        return redirect('profile')
    else:
        form = CreateUserForm()
        phone = request.POST.get('phone')
        # phone = AddPhoneNumberForm(request.POST)
        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                phone.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Profile was created for ' + user + ' Login to your Dashboard')
                return redirect('login')
          

    context = {
        'form':form
    }
    return render(request, 'registration/join.html', context)


# function that handles login route and authenticatation

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Username or password is incorrect!')
                # return render(request, 'profile', context) 

        context = {}
        return render(request, 'registration/login.html', context) 

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    
    context = {
        'name' : 'Elijah'
    }
    return render(request, 'registration/profile.html', context)
    
    
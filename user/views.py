from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import CreateUserForm


# from test import u
# Create your views here.

# def register(request):
#     form - UserCreationForm()
#     return render(request, 'main_site/join.html', {'form': form})

def join(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form':form
    }
    return render(request, 'registration/join.html', context)

def login(request):
    return render(request, 'registration/login.html', {
    })

def profile(request):
    return render(request, 'registration/profile.html', {
    })
    
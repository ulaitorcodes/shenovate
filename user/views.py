from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

# def register(request):
#     form - UserCreationForm()
#     return render(request, 'main_site/join.html', {'form': form})

def join(request):
    return render(request, 'join.html', {
        
    })

def register(request):
    return render(request, 'login.html', {
        
    })
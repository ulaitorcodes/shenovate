from django.shortcuts import render
from django.http import Http404

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.http import HttpResponse


def home(request):
    # return HttpResponse("Welcome tom Shenovate")
    return render(request, 'home.html')


def about_page(request):
    return render(request, 'about.html', {
        
    })





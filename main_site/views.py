from django.shortcuts import render
from django.http import Http404

# Create your views here.

from django.http import HttpResponse


def home(request):
    # return HttpResponse("Welcome tom Shenovate")
    return render(request, 'home.html')


def about_page(request):
    return render(request, 'about.html', {
        
    })

def join(request):
    return render(request, 'join.html', {
        
    })



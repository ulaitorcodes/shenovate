from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about_page, name="about"),
    path('join', views.join, name="join" )
]
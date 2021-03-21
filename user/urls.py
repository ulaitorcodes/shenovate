from django.urls import path

from . import views

urlpatterns = [
    path('', views.join, name="join"),
    path('register', views.register, name='signin')
]
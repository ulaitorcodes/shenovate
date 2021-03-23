from django.urls import path

from django.conf.urls import include, url

from . import views


urlpatterns = [
    path('', views.join, name="join"),
    path('/login/', views.login, name='login'),
    path('/profile/', views.profile, name='profile'),
    url('accounts/', include("django.contrib.auth.urls")),
]
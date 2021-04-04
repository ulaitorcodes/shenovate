from django.urls import path

from django.conf.urls import include, url

from . import views


urlpatterns = [
    path('', views.join, name="join"),
    path('/login/', views.loginPage, name='login'),
    path('/logout/', views.logoutUser, name='logout'),

    path('/profile/', views.profile, name='profile'),
    # url('accounts/', include("django.contrib.auth.urls")),
]

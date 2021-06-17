"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name='views.home'),
    path('tasks/', views.tasks, name='views.tasks'),
    path('items/<int:id>',views.items, name='views.items'),
    path('about/', views.about, name='views.about'),
    path('login/', views.loginpage, name='views.loginpage'),
    path('register/', views.register, name='views.register'),
    path('logout/', views.logoutpage, name='views.logoutpage'),
    ]
"""aditya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path( '',views.index, name='index'),
    path( 'contact/',views.contactme, name='contactme'),
    path( 'mlproject/', views.mlproject, name='mlproject'),
    path( 'livegame/', views.livegame, name='livegame'),
    path( 'livegame/game1/', views.game1, name='game1'),
    path( 'livegame/game2/', views.game2, name='game2'),
    path( 'livegame/game3/', views.game3, name='game3')



]

"""
URL configuration for social project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from socialapp import views
from socialapp.views import index, sobre, postar,contato,base

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('postar/', postar, name='postar'),
    path('contato/', contato, name='contato'),
    path('base/', base, name='base'),
    path('nova/', views.nova_postagem, name='nova_postagem'),
]

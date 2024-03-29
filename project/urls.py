"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from SocialTravel.views import index, mostrar_posts, agregar_post, buscar_post , mostrar_futbol, agregar_futbol, buscar_futbol, mostrar_escuela, agregar_escuela, buscar_escuela

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('mis-posts/', mostrar_posts, name="mis-posts"),
    path('mis-posts/agregar', agregar_post, name="agregar-post"),
    path('mis-posts/buscar', buscar_post, name="buscar-post"),
    path('mi-futbol/', mostrar_futbol, name="mis-futbol"),
    path('mi-futbol/agregar', agregar_futbol, name="agregar-futbol"),
    path('mi-futbol/buscar', buscar_futbol, name="buscar-futbol"),
    path('mi-escuela/', mostrar_escuela, name="mis-escuela"),
    path('mi-escuela/agregar', agregar_escuela, name="agregar-escuela"),
    path('mi-escuela/buscar', buscar_escuela, name="buscar-escuela"),
]

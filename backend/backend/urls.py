"""
URL configuration for backend project.

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
#Ten plik przekierowuje adresy URL do odpowiednich widoków lub do innych konfiguracji URL w aplikacjach.
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView 

urlpatterns = [
    path('', RedirectView.as_view(url='api/', permanent=False), name='index'),
    path('admin/', admin.site.urls), # Ścieżka do panelu administracyjnego Django
    path('api/', include('team.urls')),  # Dołączenie ścieżek URL z aplikacji 'team' pod prefixem 'api/'
]


"""baappli URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from baappli import settings
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('connexion/', connexion, name='connexion'),
    path('inscription/', inscription, name='inscription'),
    path('deconnexion/', deconnexion, name='deconnexion'),
    path('add/', add, name='ajout'),
    path('profile/', profiles, name='profile'),
    path('', index, name='index'),
    path('detail/<int:id>/', detail, name='detail'),
    path('delete/<int:id>/', delete, name='delete'),
    path('edit-profile/<int:id>/', edit_profile, name='edit_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


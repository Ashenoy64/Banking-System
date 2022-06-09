"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name="home"),
    # path("myapp",include("myapp.urls")),
    path('form', views.form, name="form"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('login', views.user_login, name="login"),
    path("check_user", views.check_user, name='check_user'),
    path("dashboard", views.dashboard, name="dashboard"),
    path("user_logout", views.user_logout, name="user_logout"),
    path("edit_profile", views.edit_profile, name="edit_profile"),
    path("change", views.change, name="change"),
    path("transfer", views.trans, name="transfer"),
]+static(settings.MEDIA_URLS, document_root=settings.MEDIA_ROOT)

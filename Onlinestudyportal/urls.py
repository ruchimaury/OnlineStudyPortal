

"""Onlinestudyportal URL Configuration

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
from general import views
from AdminZone import views as ad
urlpatterns = [
    path('admin/', admin.site.urls),
    path('online/',views.onlinestudyzone),
    path('',views.index),
    path('material/',views.Materials),
    path('Aboutus/',views.AboutUs),
    path('Contactus/',views.ContactUs),
    path('Myprofile/', views.MyProfile),
    path('Signin/', views.Signin),
    path('signup/',views.SignUp),
    path('SigninData/',views.SigninData),
    path('dashboard/',ad.dashboard),
    path('AddCources/',ad.AddCourses),
    path('AddMaterial/',ad.AddMaterial),
    path('Management/',ad.Management),
    path('Logout/',ad.Logout),
    path('ViewC/',ad.ViewC),
    path('Mts/',ad.Mts),
    path('User/', ad.User),
    path('Contact/', ad.Contact),
    path('LogOut/', ad.Logout),
    path('contactData/',views.contactData),
    path('regData/',views.regData),




]

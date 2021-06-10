#upload only those file which i changed 
#views.py

from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello World")

def aboutpage(request):
    return HttpResponse("Welcome to About Page")

def contactpage(request):
    return HttpResponse("Welcome to Contact Page")

#urls.py(for application)

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='Home'),
    path('about', views.aboutpage, name='About'),
    path('contact', views.contactpage, name='Contact')
]

#urls.py(for project)

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls'))
]

#settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp'
]

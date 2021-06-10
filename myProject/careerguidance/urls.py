from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('blog',views.blog,name='blog'),
    path('faq',views.faq,name='faq'),
    path('getintouch',views.getintouch,name='getintouch'),
    path('about',views.about,name='about'),
]

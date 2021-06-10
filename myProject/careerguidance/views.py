from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def blog(request):
    return render(request,'blog.html')

def faq(request):
    return render(request,'faq.html')

def getintouch(request):
    return render(request,'getintouch.html')

def about(request):
    return render(request,'about.html')

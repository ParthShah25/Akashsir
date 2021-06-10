from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def signin(request):
    if request.method=='POST':
        username = request.POST['User_Name']
        password = request.POST['EnterPassword']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('signin')
        
    else:
        return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['First_Name']
        last_name = request.POST['Last_Name']
        username = request.POST['User_Name']
        email = request.POST['Email_address']
        password1 = request.POST['SetPassword']
        password2 = request.POST['ConfirmPassword']

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'E-mail is already taken')
                return redirect('signup')

            if User.objects.filter(username=username).exists():
                messages.info(request,'username is already taken')
                return redirect('signup')

            else:
                user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username , password = password1, email = email)
                user.save();
                print('User Created')
                return redirect('signin')

        else:
            messages.info(request,'Password not matching')
            return redirect('signup')

        return redirect('/')

    else:    
        return render(request, 'signup.html')





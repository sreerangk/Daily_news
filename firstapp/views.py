from django.shortcuts import render
from firstapp.forms import AddressForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def index(request):
    
    
    return render(request, 'index.html')
    

def base(request):
    return render(request, 'base.html')


    
def signup(request):
    if request.method=="POST":
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['pass1']
        password2=request.POST['rpass']
        mob=request.POST['mob']
        if password==password2:
        
            if len(username)< 6:
                messages.error(request, " Your user name must minimum 6 characters")
                return redirect('signup')

            if not username.isalnum():
                messages.error(request, " User name should only contain letters and numbers")
                return redirect('signup')
            if not mob.isdigit():
                messages.error(request, "Contact number should only contain numbers")
                return redirect('signup')
            if User.objects.filter(username=username).exists():
                messages.error(request,'username is already exist')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'email is already exist')
                return redirect('signup')
            else:                                              #user creation
                user=User.objects.create_user(username=username,email=email,password=password)
 
                return redirect('login')         
        else:
            messages.error(request,'password not matching')
            return redirect('signup')
    else:

        return render(request, 'signup.html')

   

    return render(request, 'signup.html')
    
def login(request):
    return render(request, 'login.html')

def userlogin(request):
    if request.method=="post":
        user_name.request.POST=['username']
        pass_word.request.POST=['Password']
        User=auth.authenticate(username=user_name,password=pass_word)
        return redirect('index')
        if User is not None:            # means if user is authendicated
            auth.login(request,User)
            print('user not none')
            return redirect('index')
        else:
            print('failed')
            return redirect('login')
    return render(request, 'index.html')
    


def editprofile(request):
    return render(request, 'editprofile.html')


def changepassword(request):
    return render(request, 'changepassword.html')


    
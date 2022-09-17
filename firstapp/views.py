from django.shortcuts import render,redirect
from firstapp.forms import AddressForm
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login ,logout
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_authenticated:            #django authendication
        return redirect(index)
    else :
        return redirect(userlogin)
        
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')


    
def signup(request):
    if request.method=="POST":
        #username=request.POST.get('username')
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
 
                return redirect('userlogin')         
        else:
            messages.error(request,'password not matching')
            return redirect('signup')
    else:

        return render(request, 'signup.html')

   

    return render(request, 'signup.html')
    
def login(request):
    return render(request, 'login.html')

def userlogin(request):
    if request.user.is_authenticated:            #django authendication
        return redirect(index)
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:            # means if user is authendicated
            auth.login(request,user)
            return render(request, 'index.html')

        else:
            messages.error(request,'user name is inccorect')
            return redirect('userlogin')
    return render(request, 'login.html')
    
def user_logout(request):
    # if 'username' in request.session:           /// 2nd method
    if request.user.is_authenticated:
        logout(request)
        #request.session.flush()
    return redirect(userlogin)
def editprofile(request):
    return render(request, 'editprofile.html')


def changepassword(request):
    return render(request, 'changepassword.html')


    
from django.shortcuts import render
from firstapp.forms import AddressForm
from django.contrib.auth.models import User
from django.contrib import messages

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
            if len(username)<10:
                messages.error(request, " Your user name must be under 10 characters")
                return redirect('signup')

            if not username.isalnum():
                messages.error(request, " User name should only contain letters and numbers")
                return redirect('signup')
            if User.objects.filter(username=username).exists():
                messages.error(request,'username is already exist')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'email is already exist')
                return redirect('index')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                mo=u_dp(userdt=user,contact_no=mob)
                mo.save()
                user.save()
                messages.success(request,'user created')
                return redirect('login')         
        else:
            messages.error(request,'password not matching')
            return redirect('base')
    else:

        return render(request, 'signup.html')

   

    return render(request, 'signup.html')
    
def login(request):
    return render(request, 'login.html')


def editprofile(request):
    return render(request, 'editprofile.html')


def changepassword(request):
    return render(request, 'changepassword.html')


    
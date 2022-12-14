from django.shortcuts import render,redirect
from multiprocessing import context
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import u_dp,news
from django.db.models import Q
from.forms import newsForm      
# Create your views here.

def base(request):
    return render(request, 'base.html')


    
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=="POST":
        #username=request.POST.get('username')
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['pass1']
        password2=request.POST['rpass']
        mob=request.POST['mob']
        if password==password2:
        
            if len(username)< 2:
                messages.error(request, " Your user name must minimum 6 characters")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.error(request,'User name already exists')
                return redirect('signup')
            elif not username.isalnum():
                messages.error(request, " User name should only contain letters and numbers")
                return redirect('signup')
            elif not mob.isdigit():
                messages.error(request, "Contact number should only contain numbers")
                return redirect('signup')
           
            elif User.objects.filter(email=email).exists():
                messages.warning(request,'email is already exist')
                return redirect('signup')
            else:                                              #user creation
                user=User.objects.create_user(username=username,email=email,password=password)
                messages.success(request,'your account successfully created')
                mo=u_dp(userdt=user,contact_no=mob)
                mo.save()
                user.save()
                return redirect('userlogin')         
        else:
            messages.error(request,'password not matching')
            return redirect('signup')
    else:

        return render(request, 'signup.html')
    return render(request, 'signup.html')
    

def userlogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:            # means if user is authendicated
            auth.login(request,user)
            return redirect('index')
        
        else:
            messages.error(request,'user name or password inccorect')
            return redirect('userlogin')
    return render(request, 'login.html')
    
def user_logout(request):
    # if 'username' in request.session:           /// 2nd method
    if request.user.is_authenticated:
        auth.logout(request)
        #request.session.flush()
        return redirect(userlogin)

def index(request):
    if request.user.is_authenticated:
        data=u_dp.objects.all()
        products=news.objects.all()

        try:
            data=u_dp.objects.get(userdt__id=request.user.id)
        
        except u_dp.DoesNotExist:
            user = None
        context={'data':data,'products':products}

        return render(request, 'index.html',context)
    
    return render(request, 'login.html')

 
def editprofile(request):
    if request.user.is_authenticated:
        data=u_dp.objects.all()
        
        try:
            data=u_dp.objects.get(userdt__id=request.user.id)
        
        except u_dp.DoesNotExist:
            user = None
        context={'data':data}
        return render(request, 'editprofile.html',context)
     
    return render(request, 'login.html')

   
def userpro(request):
    if request.user.is_authenticated:
        data=u_dp.objects.all()
        
        try:
            data=u_dp.objects.get(userdt__id=request.user.id)
        
        except u_dp.DoesNotExist:
            user = None
        context={'data':data}
        return render(request, 'userpro.html',context)
    auth.logout(request)     
    return render(request, 'login.html')


@login_required(login_url='login')
def editauth(request):
    if request.user.is_authenticated:
        data=u_dp.objects.get(userdt__id=request.user.id)
        context={}
        context['data']=data
        if request.method=='POST':
            na=request.POST['name']
            em=request.POST['email']
            mo=request.POST['mob']
            ci=request.POST['city']
            ad=request.POST['address']
            if len(na)< 2:
                messages.error(request, " Your user name must minimum 2 characters")
                return redirect('editprofile')
            elif not na.isalnum():
                messages.error(request, " User name should only contain letters and numbers")
                return redirect('editprofile')
            elif not mo.isdigit():
                messages.error(request, "Contact number should only contain numbers")
                return redirect('editprofile')
            
            
            elif not mo.isdigit():
                messages.error(request, "Contact number should only contain numbers")
                return redirect('editprofile')
            us=User.objects.get(id=request.user.id)
            us.username=na
            us.email=em
            us.save()
            data.Address=ad
            data.contact_no=mo
            data.city=ci
            data.save()
            if "pic" in request.FILES:
                data.dp=request.FILES['pic']
                data.save()
            else:
                pass
            messages.success(request, 'profile updates successfully')
            return render(request,'userpro.html', context)
        messages.erorr(request, 'please provide valid data')
        return render(request,'editprofile.html', context)
    return render(request,'login.html', context)


    
def changepassword(request):
    if request.user.is_superuser:
        return redirect('/')
    if request.user.is_authenticated:
        data=u_dp.objects.all()
        
        try:
            data=u_dp.objects.get(userdt__id=request.user.id)
        
        except u_dp.DoesNotExist:
            user = None
        context={'data':data}
    
        return render(request,'changepassword.html',context) 
    
    return render(request, 'login.html')   


@login_required(login_url='login')
def changepasswordauth(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            oldpassword=request.POST['oldpassword']
            newpassword=request.POST['newpassword']
            newpassword2=request.POST['newpassword2']
            user = User.objects.get(username=request.user)
            check=user.check_password(oldpassword)

            if check==True:
                if newpassword==newpassword2:
                    user.set_password(newpassword)
                    user.save()
                    auth.logout(request)
                    #request.session.flush()
            
                    #messages.info(request,'password changed successfully')
                    messages.success(request,'password changed please login agin')
                    return redirect(userlogin)
                elif newpassword!=newpassword2:
                    #   messages.info(request,'password not matching')
                    messages.warning(request,'password not matching')
                    return redirect('changepasswordauth')
            else:
                # messages.info(request,'old password not matching')
                messages.error(request,'old password not matching')
                return render(request,'changepassword.html')
        
        return render(request,'changepassword.html')
    
   
    return render(request, 'login.html')

# __________________________admin edit _______________________________



def edit_user(request):
    if request.user.is_superuser:
        data=u_dp.objects.all()

        try:
            data=u_dp.objects.get(userdt__id=request.user.id)
        
        except u_dp.DoesNotExist:
            user = None
        context={'data':data}
    
        users=User.objects.all()
        
        context={'users':users}
       
        return render(request, 'edit_user.html',context)
    auth.logout(request)
    return render(request, 'login.html')

def deleteuser(request,pk):
    if request.user.is_superuser:
        user=User.objects.get(id=pk)
        user.delete()
        messages.success(request, 'Delete user sucessfully')
        return redirect('edit_user')
    auth.logout(request)
    return render(request, 'login.html')




  
def edituser_single(request,pk):
    if request.user.is_superuser:
        us=User.objects.get(id=pk)
        data=u_dp.objects.get(userdt__id=pk)
        context={'us':us}
        context['data']=data
        if request.method=='POST':
            na=request.POST['name']
            em=request.POST['email']
            mo=request.POST['mob']
            ci=request.POST['city']
            ad=request.POST['address']
            
            if len(na)< 2:
                messages.error(request, " Your user name must minimum 2 characters")
                return render(request,'edituser_single.html', context)
            elif not na.isalnum():
                messages.error(request, " User name should only contain letters and numbers")
                return render(request,'edituser_single.html', context)
            elif not mo.isdigit():
                messages.error(request, "Contact number should only contain numbers")
                return render(request,'edituser_single.html', context)
            
            
            elif not mo.isdigit():
                messages.error(request, "Contact number should only contain numbers")
                return render(request,'edituser_single.html', context)
            
            us.username=na
            us.email=em
            us.save()
            data.Address=ad
            data.contact_no=mo
            data.city=ci
            data.save()
            if "pic" in request.FILES:
                data.dp=request.FILES['pic']
                data.save()
            else:
                pass
            messages.success(request, 'profile updates successfully')
            return render(request,'edituser_single.html', context)
        
        return render(request,'edituser_single.html', context)
    
    return render(request, 'edit_user.html',context)



def blockuser(request,id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return redirect('edit_user')


def unblock(request,id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return redirect('edit_user')
     
     
     
     
def adduser(request):
    if request.user.is_superuser:
        if request.method=="POST":
            #username=request.POST.get('username')
            username=request.POST['name']
            email=request.POST['email']
            password=request.POST['pass1']
            password2=request.POST['rpass']
            mob=request.POST['mob']
            if password==password2:
            
                if len(username)< 2:
                    messages.error(request, " Your user name must minimum 2 characters")
                    return redirect('adduser')
                elif User.objects.filter(username=username).exists():
                    messages.error(request,'User name already exists')
                    return redirect('signup')
                elif not username.isalnum():
                    messages.error(request, " User name should only contain letters and numbers")
                    return redirect('adduser')
                elif not mob.isdigit():
                    messages.error(request, "Contact number should only contain numbers")
                    return redirect('adduser')
                
                elif User.objects.filter(email=email).exists():
                    messages.warning(request,'email is already exist')
                    return redirect('adduser')
                else:                                              #user creation
                    user=User.objects.create_user(username=username,email=email,password=password)
                    messages.success(request,'your account successfully created')
                    mo=u_dp(userdt=user,contact_no=mob)
                    mo.save()
                    user.save()
                    return redirect('adduser')         
            else:
                messages.error(request,'password not matching')
                return redirect('adduser')
        else:

            return render(request, 'adduser.html')
    auth.logout(request)     
        
    return render(request, 'login.html')


# -------------------------------------------------------searching------------------------------------------------------------------??




def search_user(request):
    if request.user.is_superuser:
    
        if 'q' in request.GET:
            q=request.GET['q']
            # data = User.objects .filter(username__icontains=q)
            multiple_q =Q(Q(username__icontains=q) | Q(email__icontains=q))
            users =  User.objects.filter(multiple_q)
        else:
            users = User.objects.all()
        context={
            'users':users
        }
        
        return render(request,"edit_user.html",context)
    auth.logout(request) 
    return render(request, "login.html")
    
# -----------------------------------------product inserting------------------------------------------------------------->

def news_insert(request):
    if request.user.is_superuser:
        products=news.objects.all()
        if request.method=='POST':
            form=newsForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'News Added successfully') 
                return redirect('news_insert')
        else:
            form=newsForm()

        
        context={'form':form,'products':products }
        return render(request, "news_insert.html",context)
    auth.logout(request) 
    return render(request, "login.html")


def newsdelete(request,pk):
    products=news.objects.get(id=pk)
    products.delete()
    messages.success(request, 'News Delete successfully')
    return redirect('news_insert' )

def newsedit(request,pk):  
    if request.user.is_superuser: 
        products=news.objects.get(id=pk)
        if request.method=='POST':
            form=newsForm(request.POST,request.FILES,instance=products)
            if form.is_valid():
                form.save()
                messages.success(request, 'News Updated successfully')
                return redirect('news_insert')
        else:
            form=newsForm(instance=products) 
        context={'form':form}    
        return render(request,'newsedit.html',context )
    auth.logout(request) 
    return render(request, "login.html")
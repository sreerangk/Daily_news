from django.shortcuts import render
from firstapp.forms import AddressForm

# Create your views here.
def index(request):
    
    
    return render(request, 'index.html')
    

def base(request):
    return render(request, 'base.html')

def sign_up(request):
    context = {'form': AddressForm()}
    return render(request, 'signup.html',context)
    
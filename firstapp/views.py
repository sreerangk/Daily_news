from django.shortcuts import render
from firstapp.forms import UniversityForm

# Create your views here.
def index(request):
    context = {'form': UniversityForm()}
    return render(request, 'index.html', context)
    

def base(request):
    return render(request, 'base.html')

def sign_up(request):
    return render(request, 'signup.html')
    
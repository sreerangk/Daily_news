from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import news
#for admin
class newsForm(forms.ModelForm):
    class Meta:
        model=news
        fields=['name','discriptiom', 'image']   

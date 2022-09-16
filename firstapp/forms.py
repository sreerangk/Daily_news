from django import forms
from django.contrib.auth.models import User
from . import models
#for admin
class AddressForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

from django import forms

STATES = (
    ('', 'Choose...'),
    ('kL', 'kerala'),
    ('TN', 'Tamil Nadu'),
    ('KD', 'karnadaka')
)

class AddressForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter name '}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Email id'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': 'Address'})
    )
 
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'city'}))
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter Password'}))
    check_me_out = forms.BooleanField(required=False)
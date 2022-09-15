from django import forms

STATES = (
    ('', 'Choose...'),
    ('kl', 'kerala'),
    ('TN', 'Tamil Nadu'),
    ('KD', 'karnadaka')
)

class AddressForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter name '}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Email id'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': 'Address'})
    )
 
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'city'}))
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)
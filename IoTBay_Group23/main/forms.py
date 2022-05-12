from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

SHIPPING_CHOICES = (
    ('S', 'Standard'),
    ('E', 'Express')
)

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]   

class DeleteUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [] 

class StaffForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:

        model = User
        fields = ["username", "email", "password1", "password2", "is_staff"]
    
#is_staff 
#"__all__"

class AddressForm(forms.Form):
    street_address = forms.CharField()
    city = forms.CharField()
    postcode = forms.CharField()
    country = forms.CharField()
    state = forms.CharField()
    shipping_method = forms.ChoiceField(widget=forms.RadioSelect(), choices=SHIPPING_CHOICES)
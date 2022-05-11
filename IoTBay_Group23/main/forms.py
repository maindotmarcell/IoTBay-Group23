from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django import  forms
from django.contrib.auth.models import User



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

class PaymentForm(forms.Form):
    name_on_card = forms.CharField()
    card_number = forms.IntegerField()
    expiry_date = forms.DateField()
    cvv = forms.IntegerField()
  
    
#is_staff 
#"__all__"
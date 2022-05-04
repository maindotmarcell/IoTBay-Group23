from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django import  forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class StaffForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:

        model = User
        fields = ["username", "email", "password1", "password2", "is_staff"]
    
#Staff status
#"__all__"

class UpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]   

class DeleteUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [] 
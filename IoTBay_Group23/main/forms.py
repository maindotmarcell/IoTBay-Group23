from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django import  forms
from django.contrib.auth.models import User
from .models import Payment

from django.forms import ModelForm
from .models import Item


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

class EditPaymentForm(forms.Form):
    name_on_card = forms.CharField()
    card_number = forms.IntegerField()
    expiry_date = forms.DateField()
    cvv = forms.IntegerField()


   
# class CheckoutPayment(forms.Form):
#     class Meta:
#         model = Payment
#         fields = ["name_on_card", "card_number"]
  
    
class AddItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'stock_num', 'price', 'image']

class UpdateItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'stock_num', 'price', 'image']

#is_staff 
#"__all__"
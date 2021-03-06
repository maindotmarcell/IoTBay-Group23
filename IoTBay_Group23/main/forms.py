from calendar import c
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Payment, Shipping
from django.contrib.admin.widgets import AdminDateWidget

SHIPPING_CHOICES = (("S", "Standard"), ("E", "Express"))

from django.forms import DateField, ModelForm
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


class EditPaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ["name_on_card", "card_number", "expiry_date", "cvv"]


class EditAddressForm(ModelForm):
    class Meta:
        model = Shipping
        fields = [
            "street_address",
            "city",
            "postcode",
            "country",
            "state",
            "shipping_method",
        ]


class AddItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "stock_num", "price", "image"]


class UpdateItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "stock_num", "price", "image"]


class AddressForm(forms.Form):
    street_address = forms.CharField()
    city = forms.CharField()
    postcode = forms.CharField()
    country = forms.CharField()
    state = forms.CharField()
    shipping_method = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=SHIPPING_CHOICES
    )

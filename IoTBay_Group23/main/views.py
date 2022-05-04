from ctypes.wintypes import HHOOK
from profile import Profile
from django.shortcuts import redirect, render
from django.contrib import messages
# from django.http import HttpResponse
# from .models import Customer
# from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import RegisterForm, UpdateForm, DeleteUserForm, StaffForm

from django.contrib.auth.decorators import login_required


# Create your views here.
def index(response):
    return render(response, "main/base.html", {})


def home(response):
    return render(response, "main/home.html", {})


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = RegisterForm()

    return render(response, "main/register.html", {"form": form})


def welcome(response):
    name = response.user.username
    # email = response.user.email
    email = ""
    # joined = response.user.date_joined
    joined = ""
    return render(
        response, "main/welcome.html", {"name": name, "email": email, "joined": joined}
    )


def main(response):
    return render(response, "main/main.html", {})


def logout(response):
    logout(response)
    return redirect("/home")



def edit(response):

    if response.method == "POST":   
        user_form = UpdateForm(response.POST, instance=response.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(response, f'Details Updated')
            return redirect ("/welcome")

    else:
        user_form = UpdateForm(instance=response.user)


    context = {
        'user_form': user_form
    }

    return render(response, "main/edit.html", context)

def confirmation (response):
    return render(response, "Delete_Account/confirmation.html", {})

def DeleteAccount(response):
    if response.method == 'POST':
        delete_form = DeleteUserForm(response.POST, instance = response.user)
        response.user.delete()
        #return redirect ("/login")
        return redirect ("/confirmation")

    else:
        delete_form = DeleteUserForm(instance=response.user)
        context = {'delete_form': delete_form}
    return render(response, "Delete_Account/deleteaccount.html", context)


def cart(response):
    return render(response, "main/Order_Management/cart.html")


def checkout(response):
    return render(response, "main/Order_Management/checkout.html")

def staff_registration(response):
    if response.user.is_superuser:
        if response.method == "POST":
            form = StaffForm(response.POST)
            if form.is_valid():

                form.save()


                return redirect("/welcome")
        else:
            form = StaffForm()
            context = {"form": form}
        return render(response, "registration/staff_registration.html", context)


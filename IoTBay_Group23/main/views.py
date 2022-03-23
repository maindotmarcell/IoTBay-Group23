from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm 

# Create your views here.


def index(response, id):
    cust = Customer.objects.get(id=id)
    return render(response, "main/base.html", {})


def home(response):
    return render(response, "main/home.html", {})


def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = UserCreationForm()

    return render(response, "main/register.html", {"form": form})
from django.shortcuts import redirect, render

# from django.http import HttpResponse
# from .models import Customer
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.models import User
from .forms import RegisterForm


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

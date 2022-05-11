from profile import Profile
from re import L
from django.shortcuts import redirect, render
from django.contrib import messages
# from django.http import HttpResponse
# from .models import Customer
# from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import PaymentForm, RegisterForm, UpdateForm, DeleteUserForm, StaffForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json


# Create your views here.
def index(request):
    return render(request, "main/base.html", {})


def home(request):
    return render(request, "main/home.html", {})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = RegisterForm()

    return render(request, "main/register.html", {"form": form})


def welcome(request):
    name = request.user.username
    # email = request.user.email
    email = ""
    # joined = request.user.date_joined
    joined = ""
    return render(
        request, "main/welcome.html", {"name": name, "email": email, "joined": joined}
    )


def main(request):
    products = Item.objects.all()
    context = {'products': products}
    return render(request, "main/main.html", context) 


def logout(request):
    logout(request)
    return redirect("/home")



def edit(request):

    if request.method == "POST":   
        user_form = UpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, f'Details Updated')
            return redirect ("/welcome")

    else:
        user_form = UpdateForm(instance=request.user)


    context = {
        'user_form': user_form
    }

    return render(request, "main/edit.html", context)

def edit_payment(request):
    if request.method == "POST":
        payment_form = PaymentForm(request.POST, instance=request.user)
        if payment_form.is_valid():
            payment_form.save()
            messages.success(request, f'Details Updated')
            return redirect ("/welcome")
    else:
        payment_form = PaymentForm(instance=request.user)
        context = {'payment_form': payment_form}
    return render(request, "Payment_Management/edit_payment.html", context)

def delete_payment_confirmation(request):
    return render(request, "Payment_Management/delete_payment_confirmation.html", {})

def delete_payment(request):
    return render(request, "Payment_Management/delete_payment.html", {})

def confirmation (request):
    return render(request, "Delete_Account/confirmation.html", {})

def DeleteAccount(request):
    if request.method == 'POST':
        delete_form = DeleteUserForm(request.POST, instance = request.user)
        request.user.delete()
        #return redirect ("/login")
        return redirect ("/confirmation")

    else:
        delete_form = DeleteUserForm(instance=request.user)
        context = {'delete_form': delete_form}
    return render(request, "Delete_Account/deleteaccount.html", context)


def cart(request):
    order_items = OrderItem.objects.all()
    context = {'items': order_items}
    return render(request, "Order_Management/cart.html",context)


def checkout(request):
    order_items = OrderItem.objects.all()
    context = {'items': order_items}
    return render(request, "Order_Management/checkout.html",context)

def staff_registration(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = StaffForm(request.POST)
            if form.is_valid():

                form.save()


                return redirect("/welcome")
        else:
            form = StaffForm()
            context = {"form": form}
        return render(request, "registration/staff_registration.html", context)


def updateItem(request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']

    print(f'Product ID: {productID}')
    print(f'Action: {action}')

    customer = request.user
    product = Item.objects.get(id=productID)
    order, created = Order.objects.get_or_create(customer=customer,complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order = order, item = product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse('Item was added', safe=False)
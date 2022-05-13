from profile import Profile
from django.template import RequestContext
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

# from django.http import HttpResponse
# from .models import Customer
# from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import View
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
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    products = Item.objects.all()
    context = {"products": products, "cart_items": cartItems}
    return render(request, "main/main.html", context)


def logout(request):
    logout(request)
    return redirect("/home")


def edit(request):

    if request.method == "POST":
        user_form = UpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, f"Details Updated")
            return redirect("/welcome")

    else:
        user_form = UpdateForm(instance=request.user)

    context = {"user_form": user_form}

    return render(request, "main/edit.html", context)


def edit_payment(request):
    form = EditPaymentForm
    context = {"form": form}
    if request.method == "POST":
        form = EditPaymentForm(request.POST)
        if form.is_valid():
            name_on_card = form.cleaned_data.get("name_on_card")
            card_number = form.cleaned_data.get("card_number")
            expiry_date = form.cleaned_data.get("expiry_date")
            cvv = form.cleaned_data.get("cvv")

        order, created = Order.objects.get_or_create(
            customer=request.user, complete=False
        )

        Payment.objects.filter(customer=request.user).delete()

        payment = Payment(
            order=order,
            customer=request.user,
            name_on_card=name_on_card,
            card_number=card_number,
            expiry_date=expiry_date,
            cvv=cvv,
        )
        payment.save()

    return render(request, "Payment_Management/edit_payment.html", context)


def delete_payment_confirmation(request):
    return render(request, "Payment_Management/delete_payment_confirmation.html", {})


def delete_payment(request):
    if request.method == "POST":
        Payment.objects.filter(customer=request.user).delete()
        return redirect("/delete_payment_confirmation")
    return render(request, "Payment_Management/delete_payment.html", {})


def edit_shippment(request):
    form = EditAddressForm
    context = {"form": form}
    if request.method == "POST":
        form = EditAddressForm(request.POST)
        if form.is_valid():
            street_address = form.cleaned_data.get("street_address")
            city = form.cleaned_data.get("city")
            postcode = form.cleaned_data.get("postcode")
            country = form.cleaned_data.get("country")
            state = form.cleaned_data.get("state")
            date = form.cleaned_data.get("date")
            shipping_method = form.cleaned_data.get("shipping_method")

        order, created = Order.objects.get_or_create(
            customer=request.user, complete=False
        )

        Shipping.objects.filter(user=request.user).delete()

        shipping = Shipping(
            street_address=street_address,
            user=request.user,
            city=city,
            postcode=postcode,
            country=country,
            state=state,
            date=date,
            shipping_method=shipping_method,
        )
        shipping.save()
    return render(
        request,
        "Shippment_Management/edit_shippment.html",
        context,
    )


def delete_shipping_confirmation(request):
    return render(request, "Shippment_Management/delete_shipping_confirmation.html", {})


def delete_shipping(request):
    if request.method == 'POST':
        Shipping.objects.filter(user=request.user).delete()
        return redirect('/delete_shipping_confirmation')
    return render(request, "Shippment_Management/delete_shipping.html", {})


def confirmation(request):
    return render(request, "Delete_Account/confirmation.html", {})


def DeleteAccount(request):
    if request.method == "POST":
        delete_form = DeleteUserForm(request.POST, instance=request.user)
        request.user.delete()
        # return redirect ("/login")
        return redirect("/confirmation")

    else:
        delete_form = DeleteUserForm(instance=request.user)
        context = {"delete_form": delete_form}
    return render(request, "Delete_Account/deleteaccount.html", context)


def cart(request):
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    cartTotal = order.get_cart_total
    context = {
        "items": items,
        "order": order,
        "cart_items": cartItems,
        "cart_total": cartTotal,
    }
    return render(request, "Order_Management/cart.html", context)


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = AddressForm()
        order_items = OrderItem.objects.all()
        order, created = Order.objects.get_or_create(
            customer=self.request.user, complete=False
        )
        cart_items = order.get_cart_items
        cart_total = order.get_cart_total
        context = {
            "form": form,
            "items": order_items,
            "cart_items": cart_items,
            "cart_total": cart_total,
        }
        return render(self.request, "Order_Management/checkout.html", context)

    def post(self, *args, **kwargs):
        form = AddressForm(self.request.POST or None)
        # order, created = Order.objects.get_or_create(customer=customer, complete=False)
        # order = Order.objects.get(user=self.request.user, ordered=False)
        if form.is_valid():
            street_address = form.cleaned_data.get("street_address")
            city = form.cleaned_data.get("city")
            postcode = form.cleaned_data.get("postcode")
            country = form.cleaned_data.get("country")
            state = form.cleaned_data.get("state")
            shipping_method = form.cleaned_data.get("shipping_method")

        address = Shipping(
            user=self.request.user,
            street_address=street_address,
            city=city,
            postcode=postcode,
            country=country,
            state=state,
            shipping_method=shipping_method,
        )
        address.save()
        return render(self.request, "Order_Management/checkout.html")


def staff_registration(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = StaffForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/welcome")
        else:
            form = StaffForm()
        return render(request, "registration/staff_registration.html", {"form": form})


def updateItem(request):
    data = json.loads(request.body)
    productID = data["productID"]
    action = data["action"]

    print(f"Product ID: {productID}")
    print(f"Action: {action}")

    customer = request.user
    product = Item.objects.get(id=productID)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, item=product)

    if action == "add":
        orderItem.quantity = orderItem.quantity + 1
    elif action == "remove":
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item was added", safe=False)


def products(request):
    if request.user.is_staff or request.user.is_superuser:
        items = Item.objects.all()
        context = {"items": items}
        return render(request, "Product_Management/products.html", context)


def add_item(request):
    if request.user.is_staff or request.user.is_superuser:
        if request.method == "POST":
            add_form = AddItemForm(request.POST, request.FILES)
            if add_form.is_valid():
                new_item = add_form.save(commit=False)
                new_item.save()
                return redirect("/products")

        else:
            add_form = AddItemForm()

        return render(request, "Product_Management/add_item.html", {"form": add_form})


def view_item(request, pk):
    if request.user.is_staff or request.user.is_superuser:
        item = get_object_or_404(Item, pk=pk)
        context = {"item": item}
        return render(request, "Product_management/view_item.html", context=context)


def delete_item(request, pk):
    if request.user.is_staff or request.user.is_superuser:
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return redirect("/products")


def update_item(request, pk):
    if request.user.is_staff or request.user.is_superuser:
        item = get_object_or_404(Item, pk=pk)
        if request.method == "POST":
            updateForm = UpdateItemForm(request.POST, request.FILES)
            if updateForm.is_valid():
                item.name = updateForm.data["name"]
                item.stock_num = updateForm.data["stock_num"]
                item.price = updateForm.data["price"]
                item.save()
                return redirect(f"/view_item/{pk}")

        else:
            updateForm = UpdateItemForm(instance=item)

        return render(
            request, "Product_Management/update_item.html", {"form": updateForm}
        )

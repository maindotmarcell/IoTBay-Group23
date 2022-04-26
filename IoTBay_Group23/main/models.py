from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Customer is a proxy class to the built in User object, this gives us the convenience of the bult in authentication functions, but gives us the flexibility to add our 
# class Customer(models.Model):
#     # name = models.CharField(max_length=200)
#     # password = models.CharField(max_length=40)
#     # email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     # username = models.CharField(max_length=30, unique=True)
#     # date_joined = models.DateTimeField(verbose_name="date joined", auto_now_true=True)
#     # last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
#     # is_admin = models.BooleanField(default=False)
#     # is_active = models.BooleanField(default=True)
#     # is_staff = models.BooleanField(default=False)
#     # is_superuser = models.BooleanField(default=False)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)


class Item(models.Model):
    name = models.CharField(max_length=100)
    stock_num = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    date = models.DateTimeField()

    def __str__(self):
        return self.date


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.amount


class Invoice(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    PaymentID = models.ForeignKey(Payment, on_delete=models.CASCADE)
    invoice_Number = models.CharField(max_length=100)

    def __str__(self):
        return self.invoice_Number


class Shipping(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    Tracking_Number = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.Tracking_Number

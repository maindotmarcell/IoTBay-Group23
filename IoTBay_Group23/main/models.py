from time import strftime
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

SHIPPING_CHOICES = (
    ('S', 'Standard'),
    ('E', 'Express')
)

class Item(models.Model):
    name = models.CharField(max_length=100)
    stock_num = models.IntegerField()
    price = models.FloatField(null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    date = models.DateTimeField(null=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.total_price for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name_on_card = models.CharField(max_length=100)
    card_number = models.IntegerField(default=0000-0000-0000)
    expiry_date = models.DateTimeField(null=True)
    cvv = models.IntegerField(default=000)

    def __str__(self):
        return str(self.id)




class Shipping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # orders = models.ForeignKey(Order, on_delete=models.CASCADE)
    # tracking_number = models.BigIntegerField(unique=True)
    street_address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    postcode = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)
    shipping_method = models.CharField(choices=SHIPPING_CHOICES, max_length=2, null=True)
 
    def __str__(self):
        return (f'{self.user.username}\'s address')

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.item.price * self.quantity

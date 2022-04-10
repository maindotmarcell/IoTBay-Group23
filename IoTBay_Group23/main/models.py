from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    stock_num = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.date


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.amount

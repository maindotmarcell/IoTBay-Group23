from django.contrib import admin
from .models import Item,Order,Payment, Invoice, Shipping
# Register your models here.
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Invoice)
admin.site.register(Shipping)

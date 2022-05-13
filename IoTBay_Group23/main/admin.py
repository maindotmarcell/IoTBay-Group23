from django.contrib import admin
from .models import Item, Order, Payment, Shipping

# Register your models here.
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Payment)


class ShippingAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        # 'order',
        # 'tracking_number',
        "street_address",
        "city",
        "postcode",
        "state",
        "country",
        "date",
        "shipping_method",
    ]


admin.site.register(Shipping, ShippingAdmin)

from django.contrib import admin
from .models import Customer, Product, Order, Cart, Shipping

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Shipping)

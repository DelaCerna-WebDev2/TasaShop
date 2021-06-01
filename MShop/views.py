from django.shortcuts import render
from .models import *


def shop(request):
	products = Product.objects.all()
	cont = {'products': products}
	return render(request, 'shop.html', cont)

def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		cartlist = order.cart_set.all()
	else:
		cartlist = []
	cont = {'cartlist':cartlist}
	return render(request, 'cart.html', cont)

def checkout(request):
	cont = {}
	return render(request, 'checkout.html', cont)

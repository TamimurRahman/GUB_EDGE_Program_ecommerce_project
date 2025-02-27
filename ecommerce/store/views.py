from django.shortcuts import render
from .models import * 

def store(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        # Create an empty cart for non-logged-in users
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}  # ✅ Fix Indentation

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:  # ✅ Ensure indentation is correct
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        # Create an empty cart for non-logged-in users
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}  # ✅ Fix indentation

    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)  # ✅ Render 'checkout.html'

	
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def orders(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is nothing in your cart at the moment")
        return redirect(reverse('inventoryitems'))

    order_form = OrderForm()
    template = 'orders/order.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
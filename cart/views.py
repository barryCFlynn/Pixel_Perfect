from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """ A view to return the cart page """

    return render(request, 'cart/cart.html')
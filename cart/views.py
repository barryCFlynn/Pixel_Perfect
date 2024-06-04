from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from inventory.models import InventoryItem, Size

# Create your views here.


def view_cart(request):
    """ A view to return the cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """
    inventory_item = get_object_or_404(InventoryItem, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size_id = request.POST.get('size')
    size = get_object_or_404(Size, pk=size_id)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in cart:
        if not isinstance(cart[item_id], dict):
            cart[item_id] = {'items_by_size': {}}
        if size_id in cart[item_id]['items_by_size']:
            cart[item_id]['items_by_size'][size_id] += quantity
        else:
            cart[item_id]['items_by_size'][size_id] = quantity
    else:
        cart[item_id] = {'items_by_size': {size_id: quantity}}

    request.session['cart'] = cart
    messages.success(request, f'Added {quantity} x {inventory_item.name} (Size: {size.get_size_display()}) to your cart')
    return redirect(redirect_url)

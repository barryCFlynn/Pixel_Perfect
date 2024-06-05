from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib import messages
from inventory.models import InventoryItem, Size
import logging



def view_cart(request):
    """ A view to return the cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add a specified quantity of a product, including its selected size, to the shopping cart.

    Args:
        request (HttpRequest): The HTTP request object containing POST data with 'quantity', 'size', and 'redirect_url'.
        item_id (int): The ID of the InventoryItem to add to the cart.

    Returns:
        HttpResponseRedirect: Redirects to the URL specified in 'redirect_url'.

    Raises:
        Http404: If the specified InventoryItem or Size does not exist.
    """
    inventory_item = get_object_or_404(InventoryItem, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size_id = request.POST.get('size')
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    # Log form data
    print(f"Item ID: {item_id}, Quantity: {quantity}, Size ID: {size_id}")

    size = get_object_or_404(Size, pk=size_id)

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


def update_cart(request, item_id):
    """Update the quantity of the specified product to the specified amount"""
    try:
        quantity = int(request.POST.get('quantity'))
        size_id = request.POST.get('size')
        cart = request.session.get('cart', {})

        logging.debug(f"Updating cart item: {item_id} with quantity: {quantity}, size_id: {size_id}")
        logging.debug(f"Current cart: {cart}")

        if size_id and size_id != 'null':
            size_id = int(size_id)  # Ensure size_id is an integer
            if item_id in cart:
                if size_id in cart[item_id]['items_by_size']:
                    if quantity > 0:
                        cart[item_id]['items_by_size'][size_id] = quantity
                    else:
                        del cart[item_id]['items_by_size'][size_id]
                        if not cart[item_id]['items_by_size']:
                            cart.pop(item_id)
            else:
                if quantity > 0:
                    cart[item_id] = {'items_by_size': {size_id: quantity}}
                else:
                    cart.pop(item_id, None)
        else:
            if item_id in cart:
                if quantity > 0:
                    cart[item_id] = quantity
                else:
                    cart.pop(item_id, None)
            else:
                if quantity > 0:
                    cart[item_id] = quantity

        request.session['cart'] = cart
        return redirect(reverse('view_cart'))
    except Exception as e:
        logging.error(f"Error updating cart: {e}")
        return HttpResponse(status=500)



def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""
    try:
        size_id = request.POST.get('size')
        logging.debug(f"Form data: item_id={item_id}, size_id={size_id}")

        cart = request.session.get('cart', {})

        logging.debug(f"Removing cart item: {item_id}, size_id: {size_id}")
        logging.debug(f"Current cart: {cart}")

        if size_id and size_id != 'null':
            size_id = int(size_id)  # Ensure size_id is an integer
            if item_id in cart:
                if size_id in cart[item_id]['items_by_size']:
                    del cart[item_id]['items_by_size'][size_id]
                    if not cart[item_id]['items_by_size']:
                        cart.pop(item_id)
        else:
            if item_id in cart:
                cart.pop(item_id, None)

        request.session['cart'] = cart
        logging.debug(f"Updated cart: {cart}")
        return HttpResponse(status=200)
    except Exception as e:
        logging.error(f"Error removing from cart: {e}")
        return HttpResponse(status=500)

def clear_cart(request):
    """Clear all items from the cart"""
    request.session['cart'] = {}
    return redirect('view_cart')
from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib import messages
from inventory.models import InventoryItem, Size


def view_cart(request):
    """ A view to return the cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add a specified quantity of a item, including its selected size, to the shopping cart.

    Args:
        request (HttpRequest): The HTTP request object containing POST 
        data with 'quantity', 'size', and 'redirect_url'.item_id (int):
        The ID of the InventoryItem to add to the cart.

    Returns:
        HttpResponseRedirect: Redirects to the URL specified in 'redirect_url'.

    Raises:
        Http404: If the specified InventoryItem or Size does not exist.
    """
    inventory_item = get_object_or_404(InventoryItem, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size_id = request.POST.get('size')
    size = get_object_or_404(Size, pk=size_id)
    cart = request.session.get('cart', {})

    # required to prevent item_id type as int
    item_id = str(item_id)

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

    messages.success(
            request,
            f'Added {quantity} x {inventory_item.name} (Size: {size.get_size_display()}) to your cart')
    return redirect(request.POST.get('redirect_url'))


def update_cart(request, item_id):
    """
    Update a specified quantity of a item, including its selected size, in the shopping cart.
    """
    inventory_item = get_object_or_404(InventoryItem, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size_id = request.POST.get('size')
    size = get_object_or_404(Size, pk=size_id)
    cart = request.session.get('cart', {})

    # required to prevent item_id type as int which breaks update cart
    item_id = str(item_id)

    if item_id in cart:
        if size_id in cart[item_id]['items_by_size']:
            if quantity > 0:
                cart[item_id]['items_by_size'][size_id] = quantity
                messages.success(
                    request, f'Updated {size.get_size_display()} {inventory_item.name} quantity to {cart[item_id]["items_by_size"][size_id]}')
            else:
                del cart[item_id]['items_by_size'][size_id]
                if not cart[item_id]['items_by_size']:
                    cart.pop(item_id)
                messages.success(request, f'Removed {size.get_size_display()} {inventory_item.name} from your cart')
    else:
        if quantity > 0:
            cart[item_id] = {'items_by_size': {size_id: quantity}}
            messages.success(request, f'Updated {inventory_item.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {inventory_item.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart."""
    try:
        size_id = request.POST.get('size')
        size = get_object_or_404(Size, pk=size_id)
        cart = request.session.get('cart', {})

        # required to prevent item_id type as int which breaks remove with 500 errors
        item_id = str(item_id)

        if item_id in cart:
            if size_id in cart[item_id]['items_by_size']:
                del cart[item_id]['items_by_size'][size_id]
                if not cart[item_id]['items_by_size']:
                    cart.pop(item_id)
                messages.success(request, f'Removed {size.get_size_display()} item from your cart')
            else:
                raise ValueError(f"Size ID {size_id} not found in cart for item ID {item_id}")
        else:
            raise ValueError(f"Item ID {item_id} not found in cart")

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item {item_id}: {e}')
        # Log the error
        print(f"Error removing item {item_id}: {e}")
        return HttpResponse(status=500)

def clear_cart(request):
    """Clear all items from the cart"""
    request.session['cart'] = {}
    return redirect('view_cart')
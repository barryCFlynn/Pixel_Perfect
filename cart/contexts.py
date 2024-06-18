from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from inventory.models import InventoryItem, Size


def cart_contents(request):
    """
    Retrieves the shopping cart contents from the session, calculates totals
    and delivery costs, and prepares context data for templates.

    Args:
        request (HttpRequest): The HTTP request object containing session data.

    Returns:
        dict: A dictionary with cart details including:
            - cart_items (list): List of cart items with details.
            - total (Decimal): Total cost of items.
            - inventory_item_count (int): Total number of items.
            - delivery (Decimal): Delivery cost.
            - free_delivery_delta (Decimal): Amount needed for free delivery.
            - free_delivery_threshold (Decimal): Free delivery threshold.
            - grand_total (Decimal): Total cost including delivery.
    """
    cart_items = []
    total = 0
    inventory_item_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        inventory_item = get_object_or_404(InventoryItem, pk=item_id)
        if isinstance(item_data, dict) and 'items_by_size' in item_data:
            for size_id, quantity in item_data['items_by_size'].items():
                if size_id:
                    size = get_object_or_404(Size, pk=size_id)
                    total_price = quantity * size.price
                    total += total_price
                    inventory_item_count += quantity
                    cart_items.append({
                        'item_id': item_id,
                        'size_id': size_id,
                        'size': size.get_size_display(),
                        'quantity': quantity,
                        'inventory_item': inventory_item,
                        'size_price': size.price,
                        'total_price': total_price,
                    })
        else:
            cart_items.append({
                'item_id': item_id,
                'size_id': None,
                'size': None,
                'quantity': item_data,
                'inventory_item': inventory_item,
                'size_price': 0,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'inventory_item_count': inventory_item_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    return context

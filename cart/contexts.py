from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from inventory.models import InventoryItem, Size

def cart_contents(request):
    cart_items = []
    total = 0
    inventory_item_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        inventory_item = get_object_or_404(InventoryItem, pk=item_id)
        if isinstance(item_data, dict) and 'items_by_size' in item_data:
            for size_id, quantity in item_data['items_by_size'].items():
                size = get_object_or_404(Size, pk=size_id)
                total_price = quantity * size.price
                total += total_price
                inventory_item_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'size': size.get_size_display(),
                    'quantity': quantity,
                    'inventory_item': inventory_item,
                    'size_price': size.price,
                    'total_price': total_price,
                })
        else:
            cart_items.append({
                'item_id': item_id,
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

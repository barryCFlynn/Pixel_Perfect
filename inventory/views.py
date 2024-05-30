from django.shortcuts import render, get_object_or_404
from .models import InventoryItem

# Create your views here.

def inventory_items(request):
    """ A view to return the inventory page, including sorting and search queries """

    inventoryitems = InventoryItem.objects.all()

    context = {
        'inventoryitems': inventoryitems,
    }

    return render(request, 'inventory/inventory.html', context)

def inventory_detail(request, inventoryitem_id):
    """ A view to show individual inventory item details """

    inventoryitem = get_object_or_404(InventoryItem, pk=inventoryitem_id)

    context = {
        'inventoryitem': inventoryitem,
    }

    return render(request, 'inventory/inventory_detail.html', context)

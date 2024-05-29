from django.shortcuts import render
from .models import InventoryItem

# Create your views here.

def inventory_items(request):
    """ A view to return the inventory page, including sorting and search queries """

    inventoryitems = InventoryItem.objects.all()

    context = {
        'inventoryitems': inventoryitems,
    }

    return render(request, 'inventory/inventory.html', context)
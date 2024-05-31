from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Min
from django.db.models.functions import Lower
from .models import InventoryItem, Category, Franchise

def inventory_items(request):
    """ A view to return the inventory page, including sorting and search queries """

    inventoryitems = InventoryItem.objects.all().annotate(min_price=Min('sizes__price'))
    query = None
    categories = None
    franchises = None
    artist = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                inventoryitems = inventoryitems.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__friendly_name'
            if sortkey == 'franchise':
                sortkey = 'franchise__friendly_name'
            if sortkey == 'artist':
                sortkey = 'artist'
            if sortkey == 'price':
                sortkey = 'min_price'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            inventoryitems = inventoryitems.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            inventoryitems = inventoryitems.filter(category__friendly_name__in=categories)
            categories = Category.objects.filter(friendly_name__in=categories)

        if 'franchise' in request.GET:
            franchises = request.GET['franchise'].split(',')
            inventoryitems = inventoryitems.filter(franchise__friendly_name__in=franchises)
            franchises = Franchise.objects.filter(friendly_name__in=franchises)

        if 'artist' in request.GET:
            artists = request.GET['artist'].split(',')
            inventoryitems = inventoryitems.filter(artist__in=artists)
            artists = list(set(inventoryitems.values_list('artist', flat=True)))

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('inventoryitems'))
            
            queries = (
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(keywords__icontains=query) |
                Q(category__friendly_name__icontains=query) |
                Q(franchise__friendly_name__icontains=query) |
                Q(artist__icontains=query)
            )
            inventoryitems = inventoryitems.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'inventoryitems': inventoryitems,
        'search_term': query,
        'current_categories': categories,
        'current_franchises': franchises,
        'current_artist': artist,
        'current_sorting': current_sorting,
    }

    return render(request, 'inventory/inventory.html', context)

def inventory_detail(request, inventoryitem_id):
    """ A view to show individual inventory item details """

    inventoryitem = get_object_or_404(InventoryItem, pk=inventoryitem_id)

    context = {
        'inventoryitem': inventoryitem,
    }

    return render(request, 'inventory/inventory_detail.html', context)

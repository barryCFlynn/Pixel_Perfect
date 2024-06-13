from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q, Min
from django.db.models.functions import Lower
from .models import InventoryItem, Category, Franchise
from .forms import InventoryForm
from decimal import Decimal

def inventory_items(request):
    """
    Display the inventory page with sorting and search functionality.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered inventory page.
    """
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
                return redirect(request.path)
            
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

def inventory_detail(request, item_id):
    """
    Display the details of a specific inventory item.

    Args:
        request (HttpRequest): The HTTP request object.
        item_id (int): The ID of the InventoryItem to display.

    Returns:
        HttpResponse: The rendered inventory item detail page.
    """
    inventoryitem = get_object_or_404(InventoryItem, pk=item_id)
    sizes = inventoryitem.sizes.all()
    # Check if any size contains 'Sale'
    has_sale_size = any('Sale' in size.get_size_display() for size in sizes)

    context = {
        'inventoryitem': inventoryitem,
        'has_sale_size': has_sale_size,
    }

    return render(request, 'inventory/inventory_detail.html', context)


def add_item(request):
    """ Add a item to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))


    if request.method == 'POST':
        form = InventoryForm(request.POST, request.FILES)
        if form.is_valid():
            inventoryitem = form.save()
            messages.success(request, 'Successfully added item!')
            return redirect(reverse('inventory_detail', args=[inventoryitem.id]))
        else:
            messages.error(request, 'Failed to add item. Please ensure the form is valid.')
    else:
        form = InventoryForm()

    template = 'inventory/add_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_item(request, item_id):
    """ Edit an item in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    inventoryitem = get_object_or_404(InventoryItem, pk=item_id)

    if request.method == 'POST':
        form = InventoryForm(request.POST, request.FILES, instance=inventoryitem)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated item!')
            return redirect(reverse('inventory_detail', args=[inventoryitem.id]))
        else:
            messages.error(request, 'Failed to update item. Please ensure the form is valid.')
    else:
        form = InventoryForm(instance=inventoryitem)
        messages.info(request, f'You are editing {inventoryitem.name}')

    template = 'inventory/edit_item.html'
    context = {
        'form': form,
        'inventoryitem': inventoryitem,
    }

    return render(request, template, context)

def delete_item(request, item_id):
    """ delete item in the store not viewable """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    inventoryitem = get_object_or_404(InventoryItem, pk=item_id)
    inventoryitem.delete()
    messages.success(request, 'Successfully deleted item!')
    return redirect(reverse('inventoryitems'))
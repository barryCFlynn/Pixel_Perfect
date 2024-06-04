from django.contrib import admin
from .models import InventoryItem, Category, Franchise, Size


# Register your models here.

class IventoryAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'franchise',
        'artist',
        'stock',
        'available',
        'rating',
        'keywords',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class FranchiseAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SizeAdmin(admin.ModelAdmin):
    list_display = (
        'size',
        'price',
    )
    list_filter = ('size',)
    search_fields = ('size',)

admin.site.register(InventoryItem, IventoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Franchise, FranchiseAdmin)
admin.site.register(Size, SizeAdmin)
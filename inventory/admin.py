from django.contrib import admin
from .models import InventoryItem, Category, Franchise


# Register your models here.
admin.site.register(InventoryItem)
admin.site.register(Category)
admin.site.register(Franchise)
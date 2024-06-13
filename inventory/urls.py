from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_items, name='inventoryitems'),
    path('<int:item_id>/', views.inventory_detail, name='inventory_detail'),
    path('add/', views.add_item, name='add_item'),
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
]
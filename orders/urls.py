from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.orders, name='orders'),
    path('order_success/<order_number>', views.order_success, name='order_success'),
    path('cache_order_data/', views.cache_order_data, name='cache_order_data'),
    path('wh/', webhook, name='webhook'),
]

from django.urls import path
from . import views
from .views import newsletter_signup, order_history, profile

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('newsletter_signup/', newsletter_signup, name='newsletter_signup'),
]

from django.db import models
from django_countries.fields import CountryField
import uuid
from django.conf import settings
from django.db.models import Sum
from inventory.models import InventoryItem, Size
from profiles.models import UserProfile


class Order(models.Model):
    """
    Model representing an order.

    Attributes:
    - order_number (str): Unique identifier for the order.
    - user_profile (UserProfile): User profile associated with the order.
    - full_name (str): Full name of the customer.
    - email (str): Email address of the customer.
    - phone_number (str): Phone number of the customer.
    - country (CountryField): Country of the customer.
    - postcode (str): Postal code of the customer's address.
    - town_or_city (str): Town or city of the customer's address.
    - street_address1 (str): First line of the customer's street address.
    - street_address2 (str, optional): Second line of the customer's street
    address.
    - county (str, optional): County, state, or locality of the customer's
    address.
    - date (datetime): Date and time when the order was created.
    - delivery_cost (Decimal): Cost of delivery for the order.
    - order_total (Decimal): Total cost of the order excluding delivery.
    - grand_total (Decimal): Total cost of the order including delivery.
    - original_cart (str): JSON representation of the original cart items.
    - stripe_pid (str): Stripe payment intent ID associated with the order.

    Methods:
    - _generate_order_number(): Generates a unique order number using UUID.
    - update_total(): Updates the order total and grand total including deliver
    costs.
    - save(*args, **kwargs): Overrides the default save method to set the order
    number if not already set.
    - __str__(): Returns a string representation of the order using the order
    number.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    full_name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False
    )
    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=False
    )
    country = CountryField(
        blank_label='Country *',
        null=False,
        blank=False
    )
    postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    town_or_city = models.CharField(
        max_length=40,
        null=False,
        blank=False
    )
    street_address1 = models.CharField(
        max_length=80,
        null=False,
        blank=False
    )
    street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    county = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0
    )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total')
        )['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (
                self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
            )
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Model representing a line item in an order.

    Attributes:
    - order (Order): The order to which the line item belongs.
    - inventory_item (InventoryItem): The inventory item associated with the
    line item.
    - size (Size): The size of the inventory item in the line item.
    - quantity (int): The quantity of the inventory item in the line item.
    - lineitem_total (Decimal): Total cost of the line item
    (quantity * size price).

    Methods:
    - save(*args, **kwargs): Overrides the default save method to calculate and
    set the line item total.
    - __str__(): Returns a string representation of the line item showing SKU
    and order number.
    """
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
    )
    inventory_item = models.ForeignKey(
        InventoryItem,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    size = models.ForeignKey(
        Size,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        null=False,
        blank=False,
        default=0
    )
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.quantity * self.size.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.inventory_item.sku} on order {self.order.order_number}'

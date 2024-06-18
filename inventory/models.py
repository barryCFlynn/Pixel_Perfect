import uuid
from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    Represents a category for inventory items.

    Attributes:
        name (str): The name of the category.
        friendly_name (str): The user-friendly name of the category.
    """
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """
        Returns the friendly name of the category.

        Returns:
            str: The friendly name of the category.
        """
        return self.friendly_name


class Franchise(models.Model):
    """
    Represents a franchise for inventory items.

    Attributes:
        name (str): The name of the franchise.
        friendly_name (str): The user-friendly name of the franchise.
    """
    class Meta:
        verbose_name_plural = 'Franchises'
  
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """
        Returns the friendly name of the franchise.

        Returns:
            str: The friendly name of the franchise.
        """
        return self.friendly_name


class Size(models.Model):
    """
    Represents the size and price of an inventory item.

    Attributes:
        size (str): The size identifier ('S', 'M', 'L').
        price (Decimal): The price of the item for the given size.
    """
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('SS', 'Small Sale'),
        ('MS', 'Medium Sale'),
        ('LS', 'Large Sale'),
    ]
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_size_display()} - ${self.price}"


class InventoryItem(models.Model):
    """
    Represents an inventory item available for purchase.

    Attributes:
        name (str): The name of the inventory item.
        sku (str): The SKU of the item.
        description (str): A description of the item.
        category (ForeignKey): The category the item belongs to.
        franchise (ForeignKey): The franchise the item belongs to.
        artist (str): The artist of the item.
        keywords (str): Comma-separated keywords for search.
        sizes (ManyToManyField): Available sizes for the item.
        stock (int): The stock quantity of the item.
        available (bool): Availability status of the item.
        rating (Decimal): Rating of the item.
        image (ImageField): Image of the item.
    """
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=8, unique=True, editable=False)
    description = models.TextField()
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    franchise = models.ForeignKey('Franchise', null=True, blank=True, on_delete=models.SET_NULL)
    artist = models.CharField(max_length=255)
    keywords = models.TextField(help_text="Comma-separated keywords for search")
    sizes = models.ManyToManyField(Size)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    image = CloudinaryField('image')

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = self.generate_sku()
        super().save(*args, **kwargs)

    def generate_sku(self):
        """
        Generate a unique SKU using UUID.
        """
        return str(uuid.uuid4()).replace("-", "").upper()[:8]

    def __str__(self):
        return self.name

    def get_min_price(self):
        """
        Returns the minimum price among available sizes for the item.

        Returns:
            str: The minimum price formatted to two decimal places.
        """
        min_price = self.sizes.aggregate(models.Min('price'))['price__min']
        return f"{min_price:.2f}" if min_price is not None else "0.00"

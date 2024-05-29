from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Franchise(models.Model):

    class Meta:
        verbose_name_plural = 'Franchises'
  
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Size(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_size_display()} - ${self.price}"


class InventoryItem(models.Model):
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    franchise = models.ForeignKey('Franchise', null=True, blank=True, on_delete=models.SET_NULL)
    artist = models.CharField(max_length=255)
    keywords = models.TextField(help_text="Comma-separated keywords for search")
    sizes = models.ManyToManyField(Size)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
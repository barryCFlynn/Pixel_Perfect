from django import forms
from .widgets import CustomClearableFileInput
from .models import InventoryItem, Category, Franchise, Size


class InventoryForm(forms.ModelForm):

    class Meta:
        model = InventoryItem
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        franchises = Franchise.objects.all()
        sizes = Size.objects.all()
        # Creating choices for the select dropdowns
        category_choices = [(c.id, c.get_friendly_name()) for c in categories]
        franchise_choices = [(f.id, f.get_friendly_name()) for f in franchises]
        size_choices = [(s.id, s.get_size_display()) for s in sizes]

        # Assigning choices to the respective fields
        self.fields['category'].choices = category_choices
        self.fields['franchies'].choices = franchise_choices
        self.fields['size'].choices = size_choices
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

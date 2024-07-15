from django import forms
from .widgets import CustomClearableFileInput
from .models import InventoryItem, Category, Franchise, Size


class InventoryForm(forms.ModelForm):
    """
    Form for creating or updating an inventory item.

    Attributes:
    - model: InventoryItem (defines the model for the form)
    - fields: '__all__' (includes all fields of the InventoryItem model)

    Additional Fields:
    - image: ImageField for uploading images of the item, using 
    CustomClearableFileInput widget
    - sizes: ModelMultipleChoiceField for selecting sizes using 
    CheckboxSelectMultiple widget

    Initialization:
    - Initializes the form with choices for 'category' and 'franchise' fields 
    retrieved from Category
    and Franchise models respectively. Sets CSS classes for all form fields.

    Parameters:
    *args, **kwargs: Variable length argument list and keyword arguments passed
    to the parent class initializer.

    """
    class Meta:
        model = InventoryItem
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    sizes = forms.ModelMultipleChoiceField(
        queryset=Size.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        franchises = Franchise.objects.all()

        # Creating choices for the select dropdowns
        category_choices = [(c.id, c.get_friendly_name()) for c in categories]
        franchise_choices = [(f.id, f.get_friendly_name()) for f in franchises]

        # Assigning choices to the respective fields
        self.fields['category'].choices = category_choices
        self.fields['franchise'].choices = franchise_choices
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

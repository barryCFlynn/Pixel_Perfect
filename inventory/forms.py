from django import forms
from .models import InventoryItem, Category, Franchise, Size


class InventoryForm(forms.ModelForm):

    class Meta:
        model = InventoryItem
        fields = '__all__'

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

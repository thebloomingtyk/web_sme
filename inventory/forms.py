# inventory/forms.py
from django import forms
from inventory.models import InventoryItem

# class InventoryItemForm(forms.ModelForm):
#     class Meta:
#         model = InventoryItem
#         fields = ['sku', 'description', 'stock_level', 'unit_cost', 'category', 'reorder_point']


class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['sku', 'slug', 'description', 'stock_level', 'unit_cost', 'category', 'reorder_point']
        prepopulated_fields = {'slug': ('sku',)}
        # You can customize the fields displayed in the form if needed

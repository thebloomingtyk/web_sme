from django.contrib import admin

from inventory.models import InventoryItem, Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('sku', 'description', 'stock_level', 'unit_cost', 'category', 'reorder_point', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated', 'category')
    list_editable = ('stock_level', 'unit_cost', 'reorder_point', 'available')
    prepopulated_fields = {'slug': ('sku',)}


# admin.site.register(InventoryItem)
# admin.site.register(Category)

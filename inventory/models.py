from django.db import models

# Create your models here.

# Inventory Items

# item_id (Primary Key)
# user_id (Foreign Key to Users)
# sku
# description
# stock_level
# unit_cost
# reorder_point

class InventoryItem(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    sku = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    stock_level = models.DecimalField(max_digits=12, decimal_places=2)
    unit_cost = models.DecimalField(max_digits=12, decimal_places=2)
    reorder_point = models.DecimalField(max_digits=12, decimal_places=2)
    
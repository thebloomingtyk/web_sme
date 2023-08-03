# inventory_app/models.py
from django.db import models
from django.shortcuts import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def get_absolute_url(self):
        return reverse("category_list")

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    stock_level = models.PositiveIntegerField(default=0)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    reorder_point = models.PositiveIntegerField(default=0)
    
    def get_absolute_url(self):
        return reverse("inventory_list")
    

    def __str__(self):
        return f"{self.sku} - {self.description}"

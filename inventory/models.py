# inventory/models.py
from django.db import models
from django.shortcuts import reverse
from inventory.signals import reorder_notification


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse("inventory:inventory_item_list_by_category", args=[self.slug])

    # def get_absolute_url(self):
    #     return reverse("category_list")

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    slug = models.SlugField(max_length=200)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    sku = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    stock_level = models.PositiveIntegerField(default=0)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    reorder_point = models.PositiveIntegerField(default=0)

    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('sku',)
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['-created'])
        ]

    def save(self, *args, **kwargs):
        if self.stock_level <= self.reorder_point:
            reorder_notification.send(sender=self.__class__, item=self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.sku

    def get_absolute_url(self):
        return reverse("inventory:inventory_item_detail", args=[self.id, self.slug])
    

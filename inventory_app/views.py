# inventory_app/views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import InventoryItem, Category

class InventoryItemList(ListView):
    model = InventoryItem
    template_name = 'inventory_app/inventory_list.html'
    context_object_name = 'inventory_items'

class InventoryItemCreate(CreateView):
    model = InventoryItem
    template_name = 'inventory_app/inventory_form.html'
    fields = ['sku', 'description', 'stock_level', 'unit_cost', 'category', 'reorder_point']

class InventoryItemUpdate(UpdateView):
    model = InventoryItem
    template_name = 'inventory_app/inventory_form.html'
    fields = ['sku', 'description', 'stock_level', 'unit_cost', 'category', 'reorder_point']

class InventoryItemDelete(DeleteView):
    model = InventoryItem
    template_name = 'inventory_app/inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory_list')
    
class InventoryDetailView(DetailView):
    model = InventoryItem
    context_object_name = 'item'
    template_name = 'inventory_app/inventory_detail.html'

class CategoryList(ListView):
    model = Category
    template_name = 'inventory_app/category_list.html'
    context_object_name = 'categories'

class CategoryCreate(CreateView):
    model = Category
    template_name = 'inventory_app/category_form.html'
    fields = ['name']
    
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'inventory_app/category_detail.html'


class CategoryUpdate(UpdateView):
    model = Category
    template_name = 'inventory_app/category_form.html'
    fields = ['name']

class CategoryDelete(DeleteView):
    model = Category
    template_name = 'inventory_app/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

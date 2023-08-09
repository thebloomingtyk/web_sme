# inventory/views.py
from typing import Any, Dict
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import InventoryItem, Category

# class InventoryItemList(LoginRequiredMixin, ListView):
#     model = InventoryItem
#     template_name = 'inventory/inventory_list.html'
#     context_object_name = 'inventory_items'


def inventory_item_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = InventoryItem.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = InventoryItem.objects.filter(category=category)
    return render(request, 
                      'inventory/inventory/list.html',
                    {'category': category, 'categories': categories, 'products': products})
        
def inventory_item_detail(request, id, slug):
    inventory_item = get_object_or_404(InventoryItem, id=id, slug=slug, available=True)
    return render(request, 'inventory/inventory/detail.html', {'inventory_item': inventory_item})


@login_required
def user_inventory_items(request):
    inventory_items = InventoryItem.objects.filter(user=request.user)
    return render(request, 'inventory/inventory_list.html', {'inventory_items': inventory_items})

# class InventoryItemCreate(LoginRequiredMixin, CreateView):
#     model = InventoryItem
#     template_name = 'inventory/inventory_form.html'
#     fields = ['category', 'sku', 'description', 'stock_level', 'unit_cost', 'category', 'reorder_point']
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all()
#         return context
    
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         # category_id = self.request.POST.get('category')
#         # form.instance.category_id = category_id
#         return super().form_valid(form)

class InventoryItemUpdate(LoginRequiredMixin, UpdateView):
    model = InventoryItem
    template_name = 'inventory/inventory_form.html'
    fields = ['sku', 'description', 'stock_level', 'unit_cost', 'category', 'reorder_point']

class InventoryItemDelete(LoginRequiredMixin, DeleteView):
    model = InventoryItem
    template_name = 'inventoryq/inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory_list')
    
class InventoryDetailView(DetailView):
    model = InventoryItem
    context_object_name = 'item'
    template_name = 'inventory/inventory_detail.html'

class CategoryList(ListView):
    model = Category
    template_name = 'inventory/category_list.html'
    context_object_name = 'categories'

class CategoryCreate(CreateView):
    model = Category
    template_name = 'inventory/category_form.html'
    fields = ['name']
    
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'inventory/category_detail.html'


class CategoryUpdate(UpdateView):
    model = Category
    template_name = 'inventory/category_form.html'
    fields = ['name']

class CategoryDelete(DeleteView):
    model = Category
    template_name = 'inventory/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')
    
    
    
    
# inventory/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import InventoryItemForm
from .models import InventoryItem

# @login_required
# def inventory_item_list(request):
#     items = InventoryItem.objects.all()
#     return render(request, 'inventory/inventory_item_list.html', {'items': items})


# def inventory_item_detail(request, pk):
#     item = get_object_or_404(InventoryItem, pk=pk)
#     return render(request, 'inventory/inventory_item_detail.html', {'item': item})


# @login_required
# def inventory_item_create(request):
#     if request.method == 'POST':
#         form = InventoryItemForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('inventory_item_list')
#     else:
#         form = InventoryItemForm()
#     return render(request, 'inventory_item_form.html', {'form': form})


# @login_required
# def inventory_item_update(request, pk):
#     item = get_object_or_404(InventoryItem, pk=pk)
#     if request.method == 'POST':
#         form = InventoryItemForm(request.POST, instance=item)
#         if form.is_valid():
#             form.save()
#             return redirect('inventory_item_list')
#     else:
#         form = InventoryItemForm(instance=item)
#     return render(request, 'inventory/inventory_item_form.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InventoryItemForm  # Create the form in forms.py

@login_required
def create_inventory_item(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('inventory:inventory_item_detail', item.id, item.slug)
    else:
        form = InventoryItemForm()
    
    context = {'form': form}
    return render(request, 'create_inventory_item.html', context)



# from django.shortcuts import render, redirect
# from .models import InventoryItem
# from .forms import InventoryItemForm
# from django.contrib.auth.decorators import login_required

# @login_required
# def inventory_item_create(request):
#     if request.method == 'POST':
#         form = InventoryItemForm(request.POST)
#         if form.is_valid():
#             inventory_item = form.save(commit=False)
#             inventory_item.user = request.user
#             inventory_item.save()
#             return redirect('inventory_list')
#     else:
#         form = InventoryItemForm()
    
#     context = {
#         'form': form,
#     }
#     return render(request, 'inventory/inventory_form.html', context)

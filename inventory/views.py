# inventory/views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import InventoryItem, Category

# class InventoryItemList(LoginRequiredMixin, ListView):
#     model = InventoryItem
#     template_name = 'inventory/inventory_list.html'
#     context_object_name = 'inventory_items'


@login_required
def user_inventory_items(request):
    inventory_items = InventoryItem.objects.filter(user=request.user)
    return render(request, 'inventory/inventory_list.html', {'inventory_items': inventory_items})

class InventoryItemCreate(LoginRequiredMixin, CreateView):
    model = InventoryItem
    template_name = 'inventory/inventory_form.html'
    fields = ['sku', 'description', 'stock_level', 'unit_cost', 'category', 'reorder_point']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class InventoryItemUpdate(LoginRequiredMixin, UpdateView):
    model = InventoryItem
    template_name = 'inventory/inventory_form.html'
    fields = ['sku', 'description', 'stock_level', 'unit_cost', 'category', 'reorder_point']

class InventoryItemDelete(LoginRequiredMixin, DeleteView):
    model = InventoryItem
    template_name = 'inventory/inventory_confirm_delete.html'
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


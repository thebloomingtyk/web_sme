# inventory_app/urls.py
from django.urls import path
from .views import (
    InventoryItemList,
    InventoryItemCreate,
    InventoryItemUpdate,
    InventoryItemDelete,
    CategoryList,
    CategoryCreate,
    CategoryUpdate,
    CategoryDelete,
    InventoryDetailView,
    CategoryDetailView,
)

urlpatterns = [
    path('', InventoryItemList.as_view(), name='inventory_list'),
    path('add/', InventoryItemCreate.as_view(), name='inventory_add'),
    path('detail/<int:pk>/', InventoryDetailView.as_view(), name='inventory_detail'),
    path('<int:pk>/update/', InventoryItemUpdate.as_view(), name='inventory_update'),
    path('<int:pk>/delete/', InventoryItemDelete.as_view(), name='inventory_delete'),

    path('categories/', CategoryList.as_view(), name='category_list'),
    path('categories/add/', CategoryCreate.as_view(), name='category_add'),
    path('categories/detail/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:pk>/update/', CategoryUpdate.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDelete.as_view(), name='category_delete'),
]

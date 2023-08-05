# inventory/urls.py
from django.urls import path
from . import views
from .views import (
    # InventoryItemList,
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
    
    # 
    
    # path('list/', views.inventory_item_list, name='inventory_item_list'),
    # path('<int:pk>/', views.inventory_item_detail, name='inventory_item_detail'),
    # path('create/', views.inventory_item_create, name='inventory_item_create'),
    # path('<int:pk>/update/', views.inventory_item_update, name='inventory_item_update'),
    
    
    # 
    path('', views.user_inventory_items, name='inventory_list'),
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

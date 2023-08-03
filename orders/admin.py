from django.contrib import admin

from orders.models import PurchaseOrder, SalesOrder

# Register your models here.

admin.site.register(PurchaseOrder)
admin.site.register(SalesOrder)
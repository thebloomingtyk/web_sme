from django.contrib import admin

from reports.models import InventoryReport, FinancialReport

# Register your models here.

admin.site.register(InventoryReport)
admin.site.register(FinancialReport)

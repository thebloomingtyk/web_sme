from django.db import models


# Create your models here.


class FinancialReport(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    report_type = models.CharField(max_length=50)  # e.g., profit and loss, balance sheet, cash flow
    report_date = models.DateField()
    report_data = models.JSONField()


class InventoryReport(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    report_type = models.CharField(max_length=50)  # e.g., stock levels, turnover rate, valuation
    report_date = models.DateField()
    report_data = models.JSONField()

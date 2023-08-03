from django.db import models

# Create your models here.

class CurrencyExchangeRate(models.Model):
    base_currency = models.CharField(max_length=3)
    target_currency = models.CharField(max_length=3)
    exchange_rate = models.DecimalField(max_digits=12, decimal_places=6)
    rate_date = models.DateField()
    
    
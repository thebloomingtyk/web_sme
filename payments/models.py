from django.db import models

# Create your models here.

class PaymentTransaction(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    transaction_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_gateway = models.CharField(max_length=100)
    status = models.CharField(max_length=20)  # e.g., success, failure
    # status = models.models.BooleanField(_("status"), default=False)
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
    



class PurchaseOrder(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    order_number = models.CharField(max_length=50)
    order_date = models.DateField()
    supplier_id = models.PositiveIntegerField()  # Replace with ForeignKey to Suppliers table
    status = models.CharField(max_length=20)  # e.g., pending, received
    
    
class SalesOrder(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    order_number = models.CharField(max_length=50)
    order_date = models.DateField()
    customer_id = models.PositiveIntegerField()  # Replace with ForeignKey to Customers table
    status = models.CharField(max_length=20)  # e.g., pending, shipped
    
    
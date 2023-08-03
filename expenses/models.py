from django.db import models


# Create your models here.
# Invoices

# invoice_id (Primary Key)
# user_id (Foreign Key to Users)
# invoice_number
# invoice_date
# due_date
# total_amount
# status (e.g., paid, unpaid)

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('paid', 'paid'),
        ('unpaid', 'unpaid'),
    ]
    invoice_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=10)
    invoice_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='unpaid')

    def __str__(self):
        return self.invoice_number


#     Expenses

# expense_id (Primary Key)
# user_id (Foreign Key to Users)
# expense_date
# description
# amount

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('office supplies', 'Office supplies'),
        ('travel', 'Travel'),
        ('meals and entertainment', 'Meals and entertainment'),
        ('utilities', 'Utilities'),
        ('rent', 'Rent'),
        ('payroll', 'Payroll'),
    ]

    # this one above to be removed, only for testing

    expense_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='office supplies')
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description

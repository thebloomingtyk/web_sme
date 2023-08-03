from django.db import models

# Create your models here.
# account_id (Primary Key)
# user_id (Foreign Key to Users)
# account_name
# account_type (e.g., general ledger, accounts payable, accounts receivable)
# balance

class Accounts(models.Model):
    
    ACCOUNT_CHOICES = [
        ('general ledger', 'General ledger'),
        ('accounts payable', 'Accounts payable'),
        ('accounts receivable', 'Accounts receivable'),
    ]
    
    account_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    account_name = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50, choices=ACCOUNT_CHOICES, default='general ledger')
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    
    
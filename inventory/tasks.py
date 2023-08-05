# inventory/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from ..inventory.models import InventoryItem

@shared_task
def check_reorder_points():
    items_to_reorder = InventoryItem.objects.filter(stock_level__lte=F('reorder_point'))
    
    for item in items_to_reorder:
        send_reorder_notification(item)

def send_reorder_notification(item):
    subject = f'Reorder Notification: {item.sku}'
    message = f"The stock level for {item.sku} is {item.stock_level}. It's time to reorder."
    from_email = 'your@example.com'
    recipient_list = ['recipient@example.com']

    send_mail(subject, message, from_email, recipient_list)

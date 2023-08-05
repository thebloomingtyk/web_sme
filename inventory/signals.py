# inventory/signals.py
from django.db.models.signals import Signal
from django.dispatch import receiver
from django.core.mail import send_mail

reorder_notification = Signal()

@receiver(reorder_notification)
def send_reorder_notification(sender, **kwargs):
    item = kwargs['item']
    # Implement notification logic here
    # You can use email, messaging services, or other notifications
    # Example: send an email notification
    subject = f'Reorder Notification: {item.sku}'
    message = f"The stock level for {item.sku} is {item.stock_level}. It's time to reorder."
    from_email = 'your@example.com'
    recipient_list = ['recipient@example.com']

    send_mail(subject, message, from_email, recipient_list)

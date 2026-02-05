from celery import shared_task
from .models import Notification

@shared_task
def send_notification(user_id, message):
    """
    Crée et envoie une notification à l'utilisateur.
    Peut être déclenché par des actions dans d'autres apps (mentions, likes, etc.)
    """
    Notification.objects.create(user_id=user_id, message=message)

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Trade, Wallet
from .tasks import complete_trade, update_wallet_balance

@receiver(post_save, sender=Trade)
def trigger_trade_completion(sender, instance, created, **kwargs):
    """
    Lorsqu'un Trade est créé ou mis à jour, si son status est 'pending',
    on déclenche la tâche Celery pour le compléter.
    """
    if created or instance.status == "pending":
        complete_trade.delay(instance.id)


@receiver(post_save, sender=Wallet)
def trigger_wallet_update(sender, instance, created, **kwargs):
    """
    Met à jour automatiquement le solde d'un wallet après sa création ou modification.
    """
    update_wallet_balance.delay(instance.user.id)

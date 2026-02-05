from celery import shared_task
from .models import Trade, Wallet, NFT
from .blockchain import ethereum, polygon
from django.conf import settings

@shared_task
def complete_trade(trade_id: int):
    """Effectue la transaction d'un NFT et met à jour le trade"""
    try:
        trade = Trade.objects.get(id=trade_id)
        if trade.status != "pending":
            return "Trade déjà traité"

        # Transfert sur Ethereum ou Polygon (selon configuration)
        nft = trade.nft
        seller_wallet = Wallet.objects.get(user=trade.seller)
        buyer_wallet = Wallet.objects.get(user=trade.buyer)

        if settings.BLOCKCHAIN_NETWORK == "ethereum":
            tx_hash = ethereum.send_eth(
                sender_private_key=seller_wallet.private_key,
                recipient_address=buyer_wallet.address,
                amount=float(trade.price)
            )
        else:
            tx_hash = polygon.send_matic(
                sender_private_key=seller_wallet.private_key,
                recipient_address=buyer_wallet.address,
                amount=float(trade.price)
            )

        # Mise à jour du NFT et du trade
        nft.owner = trade.buyer
        nft.is_listed = False
        nft.save()

        trade.status = "completed"
        trade.save()
        return f"Trade complété, tx_hash: {tx_hash}"

    except Trade.DoesNotExist:
        return "Trade introuvable"
    except Exception as e:
        return str(e)


@shared_task
def update_wallet_balance(user_id: int):
    """Met à jour le solde du wallet depuis la blockchain"""
    try:
        wallet = Wallet.objects.get(user_id=user_id)
        if settings.BLOCKCHAIN_NETWORK == "ethereum":
            balance = ethereum.get_balance(wallet.address)
        else:
            balance = polygon.get_balance(wallet.address)

        wallet.balance = balance
        wallet.save()
        return f"Wallet mis à jour: {balance}"
    except Wallet.DoesNotExist:
        return "Wallet introuvable"
    except Exception as e:
        return str(e)

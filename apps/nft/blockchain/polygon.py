from web3 import Web3
from django.conf import settings

# Connexion à Polygon via Infura / Alchemy
w3 = Web3(Web3.HTTPProvider(settings.POLYGON_NODE_URL))

def get_balance(address: str) -> float:
    """Retourne le solde MATIC d'une adresse"""
    balance_wei = w3.eth.get_balance(address)
    return w3.fromWei(balance_wei, 'ether')

def send_matic(sender_private_key: str, recipient_address: str, amount: float) -> str:
    """Effectue un transfert MATIC et retourne le hash de la transaction"""
    sender_account = w3.eth.account.from_key(sender_private_key)
    tx = {
        'to': recipient_address,
        'value': w3.toWei(amount, 'ether'),
        'gas': 21000,
        'gasPrice': w3.toWei('50', 'gwei'),
        'nonce': w3.eth.get_transaction_count(sender_account.address)
    }
    signed_tx = w3.eth.account.sign_transaction(tx, sender_private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash.hex()

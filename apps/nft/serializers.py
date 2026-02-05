from rest_framework import serializers
from .models import NFT, Collection, Trade, Wallet

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class NFTSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFT
        fields = '__all__'


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = '__all__'

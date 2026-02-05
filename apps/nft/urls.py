from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import NFTViewSet, CollectionViewSet, WalletViewSet, TradeViewSet

router = DefaultRouter()
router.register('collections', CollectionViewSet, basename='collection')
router.register('nfts', NFTViewSet, basename='nft')
router.register('wallets', WalletViewSet, basename='wallet')
router.register('trades', TradeViewSet, basename='trade')

urlpatterns = [
    path('', include(router.urls)),
]

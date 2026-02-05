from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Autorise uniquement le propriétaire à modifier.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Vérifie l'attribut owner pour les objets NFT/Collection/Wallet
        if hasattr(obj, 'owner'):
            return obj.owner == request.user
        if hasattr(obj, 'user'):
            return obj.user == request.user
        if hasattr(obj, 'seller'):
            return obj.seller == request.user
        return False

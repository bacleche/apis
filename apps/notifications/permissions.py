from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Autorise uniquement le propriétaire à modifier la notification.
    Les autres utilisateurs peuvent seulement lire.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

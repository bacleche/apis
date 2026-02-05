from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Autorise seulement le propriétaire de l'objet à modifier, les autres peuvent lire.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return hasattr(obj, 'creator') and obj.creator == request.user

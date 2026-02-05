from rest_framework import permissions

class IsSelfOrReadOnly(permissions.BasePermission):
    """
    Autorise l'utilisateur à modifier uniquement son propre compte.
    Les autres utilisateurs peuvent uniquement lire.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user

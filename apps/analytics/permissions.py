from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Autorise uniquement le propriétaire de l'objet ou un admin à accéder/modifier.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.user == request.user

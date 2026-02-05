from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Seuls les admins peuvent modifier (POST, PUT, PATCH, DELETE).
    Les autres utilisateurs peuvent uniquement lire.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff

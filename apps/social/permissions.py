from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Autorise uniquement l'auteur à modifier ou supprimer son objet.
    Les autres utilisateurs peuvent seulement lire.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

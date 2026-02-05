from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Autorise les utilisateurs à modifier uniquement les objets qu'ils possèdent.
    Les autres peuvent uniquement lire.
    """

    def has_object_permission(self, request, view, obj):
        # Lecture seule : GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # Vérifie si l'objet a un attribut `user` ou `creator` pour la permission
        if hasattr(obj, 'user'):
            return obj.user == request.user
        if hasattr(obj, 'creator'):
            return obj.creator == request.user
        return False

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrAdmin(BasePermission):
    """
    Permission personnalisée :
    - Lecture autorisée pour tous (GET, HEAD, OPTIONS)
    - Écriture autorisée uniquement :
        - au propriétaire de l'objet
        - ou à un administrateur
    """

    def has_object_permission(self, request, view, obj):
        # Accès en lecture pour tous
        if request.method in SAFE_METHODS:
            return True

        # Accès total pour les admins
        if request.user and request.user.is_staff:
            return True

        # Accès restreint au propriétaire
        return hasattr(obj, "owner") and obj.owner == request.user

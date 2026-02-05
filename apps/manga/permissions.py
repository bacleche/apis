from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Autorise uniquement l'auteur à modifier, sinon lecture seule.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # L'auteur du manga/chapter/page peut modifier
        if hasattr(obj, 'author'):
            return obj.author == request.user
        elif hasattr(obj, 'manga'):
            return obj.manga.author == request.user
        elif hasattr(obj, 'chapter'):
            return obj.chapter.manga.author == request.user
        return False

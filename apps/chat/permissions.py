from rest_framework import permissions

class IsParticipantOrAdmin(permissions.BasePermission):
    """
    Autorise uniquement les participants ou un admin à accéder/modifier une conversation ou message.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        if hasattr(obj, 'participants'):
            return request.user in obj.participants.all()
        if hasattr(obj, 'conversation'):
            return request.user in obj.conversation.participants.all()
        if hasattr(obj, 'user'):
            return obj.user == request.user
        return False

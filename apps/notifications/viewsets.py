from rest_framework import viewsets, permissions
from .models import Notification, NotificationPreference
from .serializers import NotificationSerializer, NotificationPreferenceSerializer
from .permissions import IsOwnerOrReadOnly


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Chaque utilisateur voit uniquement ses notifications
        return self.queryset.filter(user=self.request.user)


class NotificationPreferenceViewSet(viewsets.ModelViewSet):
    queryset = NotificationPreference.objects.all()
    serializer_class = NotificationPreferenceSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

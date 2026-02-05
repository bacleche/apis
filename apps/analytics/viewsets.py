from rest_framework import viewsets, permissions
from .models import UserActivity, ReadingStats, Engagement
from .serializers import UserActivitySerializer, ReadingStatsSerializer, EngagementSerializer
from .permissions import IsOwnerOrAdmin

class UserActivityViewSet(viewsets.ModelViewSet):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReadingStatsViewSet(viewsets.ModelViewSet):
    queryset = ReadingStats.objects.all()
    serializer_class = ReadingStatsSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EngagementViewSet(viewsets.ModelViewSet):
    queryset = Engagement.objects.all()
    serializer_class = EngagementSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

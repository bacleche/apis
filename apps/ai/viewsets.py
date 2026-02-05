from rest_framework import viewsets, permissions
from .models import Recommendation, UserPreference, MoodProfile
from .serializers import RecommendationSerializer, UserPreferenceSerializer, MoodProfileSerializer
from .permissions import IsOwnerOrAdmin

class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserPreferenceViewSet(viewsets.ModelViewSet):
    queryset = UserPreference.objects.all()
    serializer_class = UserPreferenceSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MoodProfileViewSet(viewsets.ModelViewSet):
    queryset = MoodProfile.objects.all()
    serializer_class = MoodProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

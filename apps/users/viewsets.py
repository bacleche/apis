from rest_framework import viewsets, permissions
from .models import User, Profile, Badge, Level, Achievement
from .serializers import (
    UserSerializer, UserUpdateSerializer, 
    BadgeSerializer, LevelSerializer, AchievementSerializer
)
from .permissions import IsSelfOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSelfOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return UserUpdateSerializer
        return UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        Profile.objects.create(user=user)


class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [permissions.IsAuthenticated]

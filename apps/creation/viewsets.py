from rest_framework import viewsets, permissions
from .models import UserManga, UserWebtoon, Fanfiction, Fanart
from .serializers import (
    UserMangaSerializer, UserWebtoonSerializer, FanfictionSerializer, FanartSerializer
)
from .permissions import IsOwnerOrAdmin

class UserMangaViewSet(viewsets.ModelViewSet):
    queryset = UserManga.objects.all()
    serializer_class = UserMangaSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserWebtoonViewSet(viewsets.ModelViewSet):
    queryset = UserWebtoon.objects.all()
    serializer_class = UserWebtoonSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FanfictionViewSet(viewsets.ModelViewSet):
    queryset = Fanfiction.objects.all()
    serializer_class = FanfictionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FanartViewSet(viewsets.ModelViewSet):
    queryset = Fanart.objects.all()
    serializer_class = FanartSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

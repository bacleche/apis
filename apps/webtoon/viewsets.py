from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Webtoon, Episode, Panel, Rating, Bookmark
from .serializers import WebtoonSerializer, EpisodeSerializer, PanelSerializer, RatingSerializer, BookmarkSerializer
from .permissions import IsOwnerOrReadOnly


class WebtoonViewSet(viewsets.ModelViewSet):
    queryset = Webtoon.objects.all()
    serializer_class = WebtoonSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class PanelViewSet(viewsets.ModelViewSet):
    queryset = Panel.objects.all()
    serializer_class = PanelSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

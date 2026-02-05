from rest_framework import viewsets, permissions
from .models import Manga, Chapter, Page
from .serializers import MangaSerializer, ChapterSerializer, PageSerializer
from .permissions import IsAuthorOrReadOnly

class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

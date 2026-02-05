from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import MangaViewSet, ChapterViewSet, PageViewSet

router = DefaultRouter()
router.register('mangas', MangaViewSet, basename='manga')
router.register('chapters', ChapterViewSet, basename='chapter')
router.register('pages', PageViewSet, basename='page')

urlpatterns = [
    path('', include(router.urls)),
]

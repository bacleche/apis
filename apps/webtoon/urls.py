from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import WebtoonViewSet, EpisodeViewSet, PanelViewSet, RatingViewSet, BookmarkViewSet

router = DefaultRouter()
router.register('webtoons', WebtoonViewSet, basename='webtoon')
router.register('episodes', EpisodeViewSet, basename='episode')
router.register('panels', PanelViewSet, basename='panel')
router.register('ratings', RatingViewSet, basename='rating')
router.register('bookmarks', BookmarkViewSet, basename='bookmark')

urlpatterns = [
    path('', include(router.urls)),
]

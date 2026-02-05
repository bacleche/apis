from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserMangaViewSet, UserWebtoonViewSet, FanfictionViewSet, FanartViewSet

router = DefaultRouter()
router.register('user-mangas', UserMangaViewSet, basename='usermanga')
router.register('user-webtoons', UserWebtoonViewSet, basename='userwebtoon')
router.register('fanfictions', FanfictionViewSet, basename='fanfiction')
router.register('fanarts', FanartViewSet, basename='fanart')

urlpatterns = [
    path('', include(router.urls)),
]

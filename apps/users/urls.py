from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet, BadgeViewSet, LevelViewSet, AchievementViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'badges', BadgeViewSet, basename='badge')
router.register(r'levels', LevelViewSet, basename='level')
router.register(r'achievements', AchievementViewSet, basename='achievement')

urlpatterns = [
    path('', include(router.urls)),
]

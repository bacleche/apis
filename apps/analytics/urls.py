from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserActivityViewSet, ReadingStatsViewSet, EngagementViewSet

router = DefaultRouter()
router.register('activities', UserActivityViewSet, basename='activity')
router.register('reading-stats', ReadingStatsViewSet, basename='readingstats')
router.register('engagements', EngagementViewSet, basename='engagement')

urlpatterns = [
    path('', include(router.urls)),
]

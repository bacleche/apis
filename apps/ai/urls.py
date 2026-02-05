from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import RecommendationViewSet, UserPreferenceViewSet, MoodProfileViewSet

router = DefaultRouter()
router.register('recommendations', RecommendationViewSet, basename='recommendation')
router.register('preferences', UserPreferenceViewSet, basename='preference')
router.register('mood-profiles', MoodProfileViewSet, basename='moodprofile')

urlpatterns = [
    path('', include(router.urls)),
]

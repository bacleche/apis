from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import GameViewSet, QuizViewSet, ChallengeViewSet, BattleViewSet, ScoreViewSet, LeaderboardViewSet

router = DefaultRouter()
router.register('games', GameViewSet, basename='game')
router.register('quizzes', QuizViewSet, basename='quiz')
router.register('challenges', ChallengeViewSet, basename='challenge')
router.register('battles', BattleViewSet, basename='battle')
router.register('scores', ScoreViewSet, basename='score')
router.register('leaderboard', LeaderboardViewSet, basename='leaderboard')

urlpatterns = [
    path('', include(router.urls)),
]

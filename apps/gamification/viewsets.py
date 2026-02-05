from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Game, Quiz, Challenge, Battle, Score, Leaderboard
from .serializers import (
    GameSerializer, QuizSerializer, ChallengeSerializer,
    BattleSerializer, ScoreSerializer, LeaderboardSerializer
)
from .permissions import IsOwnerOrReadOnly

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class BattleViewSet(viewsets.ModelViewSet):
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

from django.db import models
from apps.users.models import User
from apps.core.models import BaseModel

# =====================================================================
# GAMES AND QUIZZES
# =====================================================================
class Game(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Quiz(BaseModel):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='quizzes')
    question = models.TextField()
    answer = models.TextField()  # Réponse correcte
    points = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"Quiz for {self.game.title}"


# =====================================================================
# CHALLENGES
# =====================================================================
class Challenge(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    points = models.PositiveIntegerField(default=0)
    participants = models.ManyToManyField(User, through='Score', related_name='challenges')

    def __str__(self):
        return self.title


# =====================================================================
# BATTLES AND SCORES
# =====================================================================
class Battle(BaseModel):
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='battles_as_player1')
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='battles_as_player2')
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='battles_won')
    points_awarded = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.player1.username} vs {self.player2.username}"


class Score(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'challenge')


# =====================================================================
# LEADERBOARD
# =====================================================================
class Leaderboard(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_points = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-total_points']

    def __str__(self):
        return f"{self.user.username}: {self.total_points} points"

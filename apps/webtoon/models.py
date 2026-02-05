from django.db import models
from apps.users.models import User
from apps.core.models import BaseModel

# ===============================
# Webtoon principal
# ===============================
class Webtoon(BaseModel):
    title = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="webtoons")
    cover = models.ImageField(upload_to="webtoons/covers/")
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.title


# ===============================
# Episodes d'un webtoon
# ===============================
class Episode(BaseModel):
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE, related_name="episodes")
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.webtoon.title} - {self.title}"


# ===============================
# Panels (images) d'un épisode
# ===============================
class Panel(BaseModel):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name="panels")
    image = models.ImageField(upload_to="webtoons/panels/")
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Panel {self.order} of {self.episode.title}"


# ===============================
# Notation d'un webtoon par un utilisateur
# ===============================
class Rating(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="webtoon_ratings")
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE, related_name="ratings")
    score = models.PositiveIntegerField()  # 1-5 par exemple

    class Meta:
        unique_together = ('user', 'webtoon')

    def __str__(self):
        return f"{self.score} by {self.user.username} for {self.webtoon.title}"


# ===============================
# Bookmarks d'un webtoon ou épisode
# ===============================
class Bookmark(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmarks")
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE, null=True, blank=True, related_name="bookmarks")
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, null=True, blank=True, related_name="bookmarks")

    class Meta:
        unique_together = ('user', 'webtoon', 'episode')

    def __str__(self):
        if self.episode:
            return f"{self.user.username} bookmarked {self.episode.title}"
        return f"{self.user.username} bookmarked {self.webtoon.title}"

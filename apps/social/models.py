from django.db import models
from apps.users.models import User
from apps.core.models import BaseModel


class Follow(BaseModel):
    follower = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'following')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"


class Timeline(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="timeline_entries")
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Timeline entry for {self.user.username}"


class FeedPost(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Post by {self.author.username}"


class Share(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(FeedPost, on_delete=models.CASCADE, related_name="shares")

    def __str__(self):
        return f"{self.user.username} shared post {self.post.id}"


class Mention(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(FeedPost, on_delete=models.CASCADE, related_name="mentions")

    def __str__(self):
        return f"{self.user.username} mentioned in post {self.post.id}"

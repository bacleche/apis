from rest_framework import viewsets, permissions
from .models import Timeline, Follow, FeedPost, Share, Mention
from .serializers import (
    TimelineSerializer, FollowSerializer, FeedPostSerializer,
    ShareSerializer, MentionSerializer
)
from .permissions import IsAuthorOrReadOnly


class TimelineViewSet(viewsets.ModelViewSet):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]


class FeedPostViewSet(viewsets.ModelViewSet):
    queryset = FeedPost.objects.all()
    serializer_class = FeedPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


class ShareViewSet(viewsets.ModelViewSet):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer
    permission_classes = [permissions.IsAuthenticated]


class MentionViewSet(viewsets.ModelViewSet):
    queryset = Mention.objects.all()
    serializer_class = MentionSerializer
    permission_classes = [permissions.IsAuthenticated]

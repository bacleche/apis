from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ForumViewSet, ThreadViewSet, PostViewSet, CommentViewSet,
    LikeViewSet, ClubViewSet, EventViewSet, PollViewSet
)

router = DefaultRouter()
router.register('forums', ForumViewSet, basename='forum')
router.register('threads', ThreadViewSet, basename='thread')
router.register('posts', PostViewSet, basename='post')
router.register('comments', CommentViewSet, basename='comment')
router.register('likes', LikeViewSet, basename='like')
router.register('clubs', ClubViewSet, basename='club')
router.register('events', EventViewSet, basename='event')
router.register('polls', PollViewSet, basename='poll')

urlpatterns = [
    path('', include(router.urls)),
]

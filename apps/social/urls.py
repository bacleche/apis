from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TimelineViewSet, FollowViewSet, FeedPostViewSet, ShareViewSet, MentionViewSet

router = DefaultRouter()
router.register(r'timeline', TimelineViewSet, basename='timeline')
router.register(r'follows', FollowViewSet, basename='follow')
router.register(r'posts', FeedPostViewSet, basename='feedpost')
router.register(r'shares', ShareViewSet, basename='share')
router.register(r'mentions', MentionViewSet, basename='mention')

urlpatterns = [
    path('', include(router.urls)),
]

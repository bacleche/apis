from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ConversationViewSet, MessageViewSet, GroupChatViewSet, SyncReadingViewSet

router = DefaultRouter()
router.register('conversations', ConversationViewSet, basename='conversation')
router.register('messages', MessageViewSet, basename='message')
router.register('group-chats', GroupChatViewSet, basename='groupchat')
router.register('sync-readings', SyncReadingViewSet, basename='syncreading')

urlpatterns = [
    path('', include(router.urls)),
]

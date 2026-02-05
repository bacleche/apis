"""
WebSocket URL routing for MangaVerse.
Defines all WebSocket endpoints.
"""

from django.urls import path, re_path
from apps.chat.consumers import ChatConsumer, GroupChatConsumer, SyncReadingConsumer
from apps.notifications.consumers import NotificationConsumer
from apps.social.consumers import TimelineConsumer
from apps.gamification.consumers import GameConsumer

websocket_urlpatterns = [
    # Chat WebSocket endpoints
    path('ws/chat/<int:conversation_id>/', ChatConsumer.as_asgi(), name='ws_chat'),
    path('ws/chat/group/<int:group_id>/', GroupChatConsumer.as_asgi(), name='ws_group_chat'),
    
    # Synchronized reading
    path('ws/sync-reading/<int:room_id>/', SyncReadingConsumer.as_asgi(), name='ws_sync_reading'),
    
    # Notifications
    path('ws/notifications/', NotificationConsumer.as_asgi(), name='ws_notifications'),
    
    # Social timeline updates
    path('ws/timeline/', TimelineConsumer.as_asgi(), name='ws_timeline'),
    
    # Gaming (battles, quiz, etc.)
    path('ws/game/<str:game_type>/<int:game_id>/', GameConsumer.as_asgi(), name='ws_game'),
]

print("✅ WebSocket routing configured")
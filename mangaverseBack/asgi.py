"""
ASGI config for MangaVerse project.
Handles both HTTP and WebSocket connections.
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mangaverse.settings.development')

# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

# Import routing after Django is initialized
from mangaverseBack.routing import websocket_urlpatterns

# Custom middleware for WebSocket authentication
class TokenAuthMiddleware:
    """
    Custom middleware to authenticate WebSocket connections using JWT tokens
    """
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        from channels.db import database_sync_to_async
        from rest_framework_simplejwt.tokens import AccessToken
        from apps.users.models import User
        
        # Get token from query string
        query_string = scope.get('query_string', b'').decode()
        token = None
        
        for param in query_string.split('&'):
            if param.startswith('token='):
                token = param.split('=')[1]
                break
        
        # Authenticate user
        if token:
            try:
                access_token = AccessToken(token)
                user_id = access_token['user_id']
                
                @database_sync_to_async
                def get_user(user_id):
                    try:
                        return User.objects.get(id=user_id)
                    except User.DoesNotExist:
                        return None
                
                user = await get_user(user_id)
                scope['user'] = user if user else scope.get('user')
            except Exception as e:
                print(f"WebSocket authentication error: {e}")
                scope['user'] = scope.get('user')
        
        return await self.app(scope, receive, send)


def TokenAuthMiddlewareStack(app):
    """Wrapper for token auth middleware"""
    return TokenAuthMiddleware(AuthMiddlewareStack(app))


# ASGI Application
application = ProtocolTypeRouter({
    # HTTP requests
    "http": django_asgi_app,
    
    # WebSocket connections
    "websocket": AllowedHostsOriginValidator(
        TokenAuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)
        )
    ),
})

print("✅ ASGI application configured")
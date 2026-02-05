"""
URL configuration for MangaVerse project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# API version prefix
API_V1 = 'api/v1/'

urlpatterns = [
    # ============================================================================
    # ADMIN
    # ============================================================================
    path(settings.ADMIN_URL if hasattr(settings, 'ADMIN_URL') else 'admin/', admin.site.urls),
    
    # ============================================================================
    # API DOCUMENTATION
    # ============================================================================
    
    path(f'{API_V1}schema/', SpectacularAPIView.as_view(), name='schema'),
    path(f'{API_V1}docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path(f'{API_V1}redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    # ============================================================================
    # AUTHENTICATION
    # ============================================================================
    path(f'{API_V1}auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{API_V1}auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(f'{API_V1}auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path(f'{API_V1}auth/', include('dj_rest_auth.urls')),
    path(f'{API_V1}auth/registration/', include('dj_rest_auth.registration.urls')),
    path(f'{API_V1}auth/social/', include('allauth.urls')),
    
    # ============================================================================
    # CORE APPS
    # ============================================================================
    path(f'{API_V1}users/', include('apps.users.urls')),
    path(f'{API_V1}manga/', include('apps.manga.urls')),
    path(f'{API_V1}webtoon/', include('apps.webtoon.urls')),
    path(f'{API_V1}community/', include('apps.community.urls')),
    path(f'{API_V1}social/', include('apps.social.urls')),
    path(f'{API_V1}chat/', include('apps.chat.urls')),
    path(f'{API_V1}notifications/', include('apps.notifications.urls')),
    path(f'{API_V1}creation/', include('apps.creation.urls')),
    path(f'{API_V1}ai/', include('apps.ai.urls')),
    path(f'{API_V1}gamification/', include('apps.gamification.urls')),
    path(f'{API_V1}nft/', include('apps.nft.urls')),
    path(f'{API_V1}moderation/', include('apps.moderation.urls')),
    path(f'{API_V1}analytics/', include('apps.analytics.urls')),
    
    # ============================================================================
    # WEBHOOKS
    # ============================================================================
   # path('webhooks/stripe/', include('apps.nft.webhooks')),
    
    # ============================================================================
    # HEALTH CHECK
    # ============================================================================
    # path('health/', include('health_check.urls')),
    # path('api/health/', include('apps.core.urls')),
]

# Admin customization
admin.site.site_header = "MangaVerse Administration"
admin.site.site_title = "MangaVerse Admin Portal"
admin.site.index_title = "Welcome to MangaVerse Admin"

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    # Django Debug Toolbar
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns

# Custom error handlers
handler404 = 'apps.core.views.error_404'
handler500 = 'apps.core.views.error_500'
handler403 = 'apps.core.views.error_403'
handler400 = 'apps.core.views.error_400'

print("✅ URL routing configured")
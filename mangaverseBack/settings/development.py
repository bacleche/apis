"""
Development settings for MangaVerse project.
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', '*']

# Development-specific apps
INSTALLED_APPS += [
    'django_extensions',
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Debug Toolbar Configuration
INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG,
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# Database - Development
# Use SQLite for quick local development (optional)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



# Email Backend - Console for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disable real email sending in development
ACCOUNT_EMAIL_VERIFICATION = 'optional'

# Logging - More verbose in development
LOGGING['loggers']['django']['level'] = 'DEBUG'
LOGGING['loggers']['apps']['level'] = 'DEBUG'

# Add SQL query logging
LOGGING['loggers']['django.db.backends'] = {
    'handlers': ['console'],
    'level': 'DEBUG',
    'propagate': False,
}

# CORS - Allow all origins in development
CORS_ALLOW_ALL_ORIGINS = True

# Session & Cookie - Less strict in development
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = False

# Celery - Eager execution in development (no need for worker)
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# Cache - Dummy cache for development (optional)
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#     }
# }

# Static & Media - Local storage
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Development-specific settings
SHELL_PLUS_PRINT_SQL = True
SHELL_PLUS = "ipython"

# Disable SSL redirect
SECURE_SSL_REDIRECT = False

# Password hashers - Faster hashing for development
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# GraphQL settings (if using)
GRAPHENE = {
    'SCHEMA': 'mangaverseBack.schema.schema',
    'MIDDLEWARE': [
        'graphene_django.debug.DjangoDebugMiddleware',
    ],
}

# Development REST Framework settings
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
)

# Spectacular settings for development
SPECTACULAR_SETTINGS['SERVERS'] = [
    {'url': 'http://localhost:8000', 'description': 'Development server'},
    {'url': 'http://127.0.0.1:8000', 'description': 'Local development server'},
]

# Django Extensions
GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}

# Development-specific feature flags
FEATURES = {
    'ENABLE_NFT': True,
    'ENABLE_AI_RECOMMENDATIONS': True,
    'ENABLE_GAMIFICATION': True,
    'ENABLE_SOCIAL_LOGIN': True,
    'ENABLE_SYNC_READING': True,
    'ENABLE_VOICE_CHAT': False,  # Disabled in dev by default
}

print("🔧 Development settings loaded")
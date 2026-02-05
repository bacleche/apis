"""
Production settings for MangaVerse project.
Optimized for performance, security, and scalability.
"""

from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.redis import RedisIntegration

# ============================================================================
# SECURITY SETTINGS
# ============================================================================

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Allowed hosts
ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='mangaverse.com,www.mangaverse.com,api.mangaverse.com',
    cast=lambda v: [s.strip() for s in v.split(',')]
)

# SSL/HTTPS Settings
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# XSS Protection
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Cookie Security
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Strict'
SESSION_COOKIE_NAME = 'mangaverse_sessionid'
SESSION_COOKIE_AGE = 1209600  # 2 weeks

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SAMESITE = 'Strict'
CSRF_COOKIE_NAME = 'mangaverse_csrftoken'

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    'https://mangaverse.com',
    'https://www.mangaverse.com',
    'https://api.mangaverse.com',
    'https://admin.mangaverse.com',
]

# Referrer Policy
SECURE_REFERRER_POLICY = 'same-origin'

# ============================================================================
# DATABASE CONFIGURATION
# ============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default='5432'),
        'ATOMIC_REQUESTS': True,
        'CONN_MAX_AGE': 600,  # 10 minutes
        'OPTIONS': {
            'connect_timeout': 10,
            'options': '-c statement_timeout=30000',  # 30 seconds
            'sslmode': 'require',
        },
        'DISABLE_SERVER_SIDE_CURSORS': True,
    }
}

# Read Replica (Optional - for scaling reads)
if config('DB_REPLICA_HOST', default=''):
    DATABASES['replica'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_REPLICA_USER', default=config('DB_USER')),
        'PASSWORD': config('DB_REPLICA_PASSWORD', default=config('DB_PASSWORD')),
        'HOST': config('DB_REPLICA_HOST'),
        'PORT': config('DB_REPLICA_PORT', default='5432'),
        'CONN_MAX_AGE': 600,
        'OPTIONS': {
            'connect_timeout': 10,
            'sslmode': 'require',
        },
    }
    
    # Database Router for read/write splitting
    DATABASE_ROUTERS = ['apps.core.db_router.PrimaryReplicaRouter']

# ============================================================================
# CACHE CONFIGURATION
# ============================================================================

REDIS_HOST = config('REDIS_HOST')
REDIS_PORT = config('REDIS_PORT', default=6379, cast=int)
REDIS_PASSWORD = config('REDIS_PASSWORD', default='')
REDIS_DB = config('REDIS_DB', default=0, cast=int)

REDIS_URL = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}' if REDIS_PASSWORD else f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 100,
                'retry_on_timeout': True,
                'socket_keepalive': True,
                'socket_keepalive_options': {
                    1: 1,  # TCP_KEEPIDLE
                    2: 1,  # TCP_KEEPINTVL
                    3: 3,  # TCP_KEEPCNT
                },
            },
            'SOCKET_CONNECT_TIMEOUT': 5,
            'SOCKET_TIMEOUT': 5,
            'COMPRESSOR': 'django_redis.compressors.zlib.ZlibCompressor',
            'IGNORE_EXCEPTIONS': True,
        },
        'KEY_PREFIX': 'mangaverse',
        'TIMEOUT': 300,
    },
    'sessions': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 50,
            },
        },
        'KEY_PREFIX': 'session',
        'TIMEOUT': 86400,  # 24 hours
    },
    'throttle': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/2',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'KEY_PREFIX': 'throttle',
    }
}

# Session Configuration
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'sessions'

# ============================================================================
# CELERY CONFIGURATION
# ============================================================================

CELERY_BROKER_URL = config('CELERY_BROKER_URL', default=f'redis://{REDIS_HOST}:{REDIS_PORT}/3')
CELERY_RESULT_BACKEND = config('CELERY_RESULT_BACKEND', default=f'redis://{REDIS_HOST}:{REDIS_PORT}/4')

# Celery Production Settings
CELERY_TASK_ALWAYS_EAGER = False
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_WORKER_PREFETCH_MULTIPLIER = 4
CELERY_WORKER_MAX_TASKS_PER_CHILD = 1000
CELERY_WORKER_DISABLE_RATE_LIMITS = False
CELERY_TASK_ACKS_LATE = True
CELERY_TASK_REJECT_ON_WORKER_LOST = True
CELERY_WORKER_SEND_TASK_EVENTS = True
CELERY_TASK_SEND_SENT_EVENT = True

# Celery Beat
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# Broker Settings
CELERY_BROKER_TRANSPORT_OPTIONS = {
    'visibility_timeout': 3600,
    'fanout_prefix': True,
    'fanout_patterns': True,
}

# Result Backend Settings
CELERY_RESULT_BACKEND_TRANSPORT_OPTIONS = {
    'master_name': 'mymaster',
    'retry_on_timeout': True,
}

# ============================================================================
# DJANGO CHANNELS (WebSocket)
# ============================================================================

ASGI_APPLICATION = 'mangaverseBack.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [(REDIS_HOST, REDIS_PORT)],
            'capacity': 3000,
            'expiry': 10,
            'group_expiry': 86400,
            'symmetric_encryption_keys': [config('CHANNEL_ENCRYPTION_KEY', default=SECRET_KEY)],
        },
    },
}

# ============================================================================
# EMAIL CONFIGURATION
# ============================================================================

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', default='smtp.sendgrid.net')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='apikey')
EMAIL_HOST_PASSWORD = config('SENDGRID_API_KEY')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='noreply@mangaverse.com')
SERVER_EMAIL = config('SERVER_EMAIL', default='server@mangaverse.com')

# ============================================================================
# STATIC & MEDIA FILES (AWS S3 / CloudFront)
# ============================================================================

USE_S3 = config('USE_S3', default=True, cast=bool)

if USE_S3:
    # AWS Credentials
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME', default='us-east-1')
    
    # CloudFront CDN
    AWS_S3_CUSTOM_DOMAIN = config('AWS_CLOUDFRONT_DOMAIN', default=f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com')
    
    # S3 Settings
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
        'ACL': 'public-read',
    }
    AWS_DEFAULT_ACL = 'public-read'
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_FILE_OVERWRITE = False
    AWS_IS_GZIPPED = True
    AWS_S3_SIGNATURE_VERSION = 's3v4'
    
    # GZIP Content Types
    GZIP_CONTENT_TYPES = (
        'text/css',
        'text/javascript',
        'application/javascript',
        'application/x-javascript',
        'image/svg+xml',
    )
    
    # Static files
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
    
    # Media files
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
    
else:
    # Local storage fallback
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    MEDIA_ROOT = BASE_DIR / 'media'

# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{levelname}] {asctime} {name} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '[{levelname}] {message}',
            'style': '{',
        },
        'json': {
            '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'format': '%(asctime)s %(name)s %(levelname)s %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/mangaverse/django.log',
            'maxBytes': 1024 * 1024 * 15,  # 15 MB
            'backupCount': 10,
            'formatter': 'verbose',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/mangaverse/error.log',
            'maxBytes': 1024 * 1024 * 15,  # 15 MB
            'backupCount': 10,
            'formatter': 'verbose',
        },
        'celery_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/mangaverse/celery.log',
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'security_file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/mangaverse/security.log',
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 10,
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['error_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['security_file', 'mail_admins'],
            'level': 'WARNING',
            'propagate': False,
        },
        'celery': {
            'handlers': ['celery_file', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.moderation': {
            'handlers': ['file', 'security_file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# ============================================================================
# SENTRY INTEGRATION (Error Tracking)
# ============================================================================

SENTRY_DSN = config('SENTRY_DSN', default='')

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[
            DjangoIntegration(),
            CeleryIntegration(),
            RedisIntegration(),
        ],
        
        # Performance Monitoring
        traces_sample_rate=0.1,  # 10% of transactions
        
        # Error Sampling
        sample_rate=1.0,  # 100% of errors
        
        # Environment
        environment='production',
        release=config('RELEASE_VERSION', default='1.0.0'),
        
        # PII
        send_default_pii=False,
        
        # Before Send
        before_send=lambda event, hint: event if event.get('level') != 'info' else None,
        
        # Ignore certain errors
        ignore_errors=[
            KeyboardInterrupt,
        ],
    )

# ============================================================================
# REST FRAMEWORK (Production Optimizations)
# ============================================================================

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
)

REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {
    'anon': '100/hour',
    'user': '2000/hour',
    'burst': '60/minute',
    'sustained': '1000/day',
}

REST_FRAMEWORK['DEFAULT_THROTTLE_CLASSES'] = (
    'rest_framework.throttling.AnonRateThrottle',
    'rest_framework.throttling.UserRateThrottle',
    'rest_framework.throttling.ScopedRateThrottle',
)

# ============================================================================
# CORS CONFIGURATION
# ============================================================================

CORS_ALLOWED_ORIGINS = config(
    'CORS_ALLOWED_ORIGINS',
    default='https://mangaverse.com,https://www.mangaverse.com',
    cast=lambda v: [s.strip() for s in v.split(',')]
)

CORS_ALLOW_CREDENTIALS = True

# ============================================================================
# ADMIN CONFIGURATION
# ============================================================================

ADMINS = [
    ('Admin Team', config('ADMIN_EMAIL', default='admin@mangaverse.com')),
    ('DevOps', config('DEVOPS_EMAIL', default='devops@mangaverse.com')),
]

MANAGERS = ADMINS

# Admin URL (custom for security)
ADMIN_URL = config('ADMIN_URL', default='admin/')

# ============================================================================
# PASSWORD HASHERS (Strong Algorithms)
# ============================================================================

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# ============================================================================
# CONTENT SECURITY POLICY
# ============================================================================

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'", 'cdn.jsdelivr.net', 'cdnjs.cloudflare.com')
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", 'fonts.googleapis.com', 'cdn.jsdelivr.net')
CSP_FONT_SRC = ("'self'", 'fonts.gstatic.com', 'cdn.jsdelivr.net')
CSP_IMG_SRC = ("'self'", 'data:', 'https:', AWS_S3_CUSTOM_DOMAIN if USE_S3 else '')
CSP_CONNECT_SRC = ("'self'", 'wss:', 'https:', 'api.mangaverse.com')
CSP_FRAME_ANCESTORS = ("'none'",)
CSP_BASE_URI = ("'self'",)
CSP_FORM_ACTION = ("'self'",)

# ============================================================================
# API DOCUMENTATION (DRF Spectacular)
# ============================================================================

SPECTACULAR_SETTINGS = {
    'TITLE': 'MangaVerse API',
    'DESCRIPTION': 'Complete API Documentation for MangaVerse Platform',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
    'SCHEMA_PATH_PREFIX': '/api/v1',
    'SERVERS': [
        {'url': 'https://api.mangaverse.com', 'description': 'Production server'},
        {'url': 'https://api-staging.mangaverse.com', 'description': 'Staging server'},
    ],
    'EXTERNAL_DOCS': {
        'description': 'Full Documentation',
        'url': 'https://docs.mangaverse.com',
    },
}

# ============================================================================
# THIRD-PARTY SERVICES
# ============================================================================

# Stripe
STRIPE_PUBLIC_KEY = config('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY')
STRIPE_WEBHOOK_SECRET = config('STRIPE_WEBHOOK_SECRET')
STRIPE_LIVE_MODE = True

# OpenAI
OPENAI_API_KEY = config('OPENAI_API_KEY', default='')
OPENAI_MODEL = config('OPENAI_MODEL', default='gpt-4')
OPENAI_MAX_TOKENS = 2000

# Blockchain (Ethereum/Polygon)
WEB3_PROVIDER_URI = config('WEB3_PROVIDER_URI')
CONTRACT_ADDRESS = config('CONTRACT_ADDRESS')
PRIVATE_KEY = config('PRIVATE_KEY')
NETWORK_ID = config('NETWORK_ID', default=1, cast=int)  # 1 = Ethereum Mainnet

# ============================================================================
# FEATURE FLAGS
# ============================================================================

FEATURES = {
    'ENABLE_NFT': config('ENABLE_NFT', default=True, cast=bool),
    'ENABLE_AI_RECOMMENDATIONS': config('ENABLE_AI', default=True, cast=bool),
    'ENABLE_GAMIFICATION': config('ENABLE_GAMIFICATION', default=True, cast=bool),
    'ENABLE_SOCIAL_LOGIN': config('ENABLE_SOCIAL_LOGIN', default=True, cast=bool),
    'ENABLE_SYNC_READING': config('ENABLE_SYNC_READING', default=True, cast=bool),
    'ENABLE_VOICE_CHAT': config('ENABLE_VOICE_CHAT', default=True, cast=bool),
    'MAINTENANCE_MODE': config('MAINTENANCE_MODE', default=False, cast=bool),
    'ENABLE_REGISTRATION': config('ENABLE_REGISTRATION', default=True, cast=bool),
}

# ============================================================================
# PERFORMANCE & MONITORING
# ============================================================================

# Database Query Optimization
CONN_MAX_AGE = 600
ATOMIC_REQUESTS = True

# Middleware Caching
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_KEY_PREFIX = 'middleware'

# Prometheus Metrics
PROMETHEUS_METRICS_EXPORT_PORT = config('PROMETHEUS_PORT', default=8001, cast=int)
PROMETHEUS_METRICS_EXPORT_ADDRESS = ''

# Health Check
HEALTH_CHECK = {
    'DISK_USAGE_MAX': 90,  # Percent
    'MEMORY_MIN': 100,  # MB
    'DB_CONNECTION_MAX_AGE': 60,  # Seconds
}

# ============================================================================
# BACKUP & DISASTER RECOVERY
# ============================================================================

BACKUP_ROOT = config('BACKUP_ROOT', default='/var/backups/mangaverseBack')
BACKUP_COUNT = 30  # Keep 30 days of backups
BACKUP_SCHEDULE = '0 2 * * *'  # Daily at 2 AM

# ============================================================================
# RATE LIMITING
# ============================================================================

RATELIMIT_ENABLE = True
RATELIMIT_USE_CACHE = 'throttle'
RATELIMIT_VIEW = 'apps.core.views.ratelimit_view'

# ============================================================================
# DATA RETENTION
# ============================================================================

# Notification retention
NOTIFICATION_EXPIRY_DAYS = 30

# Session retention
SESSION_COOKIE_AGE = 1209600  # 2 weeks

# Log retention
LOG_RETENTION_DAYS = 90

# Deleted user data retention
DELETED_USER_DATA_RETENTION_DAYS = 30

# ============================================================================
# FRONTEND CONFIGURATION
# ============================================================================

FRONTEND_URL = config('FRONTEND_URL', default='https://mangaverse.com')
FRONTEND_CALLBACK_URL = f'{FRONTEND_URL}/auth/callback'

# ============================================================================
# CUSTOM SETTINGS
# ============================================================================

# File size limits
MAX_UPLOAD_SIZE = 50 * 1024 * 1024  # 50 MB
MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10 MB

# Pagination
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# Content moderation
AUTO_MODERATION_ENABLED = True
MODERATION_CONFIDENCE_THRESHOLD = 0.85

# Gamification
XP_MULTIPLIER_PREMIUM = 1.5

print("🚀 Production settings loaded successfully")
"""
WSGI config for MangaVerse project.
Handles traditional HTTP requests (for production with Gunicorn/uWSGI).
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mangaverse.settings.production')

application = get_wsgi_application()

print("✅ WSGI application loaded")
"""
Celery configuration for MangaVerse project.
Handles all asynchronous tasks and scheduled jobs.
"""

import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mangaverse.settings.development')

app = Celery('mangaverse')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Celery Beat Schedule - Scheduled Tasks
app.conf.beat_schedule = {
    # Send daily digest notifications at 9 AM
    'send-daily-digest': {
        'task': 'apps.notifications.tasks.send_daily_digest',
        'schedule': crontab(hour=9, minute=0),
        'options': {'queue': 'notifications'},
    },
    
    # Update trending manga every hour
    'update-trending-manga': {
        'task': 'apps.manga.tasks.update_trending',
        'schedule': crontab(minute=0),  # Every hour
        'options': {'queue': 'default'},
    },
    
    # Update leaderboards every 6 hours
    'update-leaderboards': {
        'task': 'apps.gamification.tasks.update_leaderboards',
        'schedule': crontab(hour='*/6'),
        'options': {'queue': 'gamification'},
    },
    
    # Clean up old notifications (weekly)
    'cleanup-old-notifications': {
        'task': 'apps.notifications.tasks.cleanup_old_notifications',
        'schedule': crontab(day_of_week=0, hour=2, minute=0),  # Sunday at 2 AM
        'options': {'queue': 'maintenance'},
    },
    
    # Clean up expired sessions (daily)
    'cleanup-expired-sessions': {
        'task': 'apps.core.tasks.cleanup_expired_sessions',
        'schedule': crontab(hour=3, minute=0),
        'options': {'queue': 'maintenance'},
    },
    
    # Generate AI recommendations (every 12 hours)
    'generate-ai-recommendations': {
        'task': 'apps.ai.tasks.generate_recommendations_batch',
        'schedule': crontab(hour='*/12'),
        'options': {'queue': 'ai'},
    },
    
    # Process reading statistics (daily)
    'process-reading-stats': {
        'task': 'apps.analytics.tasks.process_daily_stats',
        'schedule': crontab(hour=1, minute=0),
        'options': {'queue': 'analytics'},
    },
    
    # Backup database (daily at 2 AM)
    'backup-database': {
        'task': 'apps.core.tasks.backup_database',
        'schedule': crontab(hour=2, minute=0),
        'options': {'queue': 'maintenance'},
    },
    
    # Check and award badges (every 4 hours)
    'check-award-badges': {
        'task': 'apps.gamification.tasks.check_and_award_badges',
        'schedule': crontab(hour='*/4'),
        'options': {'queue': 'gamification'},
    },
    
    # Send reminder notifications for unfinished manga
    'send-reading-reminders': {
        'task': 'apps.notifications.tasks.send_reading_reminders',
        'schedule': crontab(day_of_week=[1, 4], hour=18, minute=0),  # Monday & Thursday at 6 PM
        'options': {'queue': 'notifications'},
    },
    
    # Update NFT metadata from blockchain (every 30 minutes)
    'sync-nft-metadata': {
        'task': 'apps.nft.tasks.sync_blockchain_metadata',
        'schedule': crontab(minute='*/30'),
        'options': {'queue': 'blockchain'},
    },
    
    # Auto-moderate new content (every 15 minutes)
    'auto-moderate-content': {
        'task': 'apps.moderation.tasks.auto_moderate_pending_content',
        'schedule': crontab(minute='*/15'),
        'options': {'queue': 'moderation'},
    },
    
    # Update user levels based on XP (hourly)
    'update-user-levels': {
        'task': 'apps.users.tasks.update_user_levels',
        'schedule': crontab(minute=30),
        'options': {'queue': 'gamification'},
    },
    
    # Generate weekly reports (Monday at 8 AM)
    'generate-weekly-reports': {
        'task': 'apps.analytics.tasks.generate_weekly_reports',
        'schedule': crontab(day_of_week=1, hour=8, minute=0),
        'options': {'queue': 'analytics'},
    },
    
    # Clean up temporary files (daily)
    'cleanup-temp-files': {
        'task': 'apps.core.tasks.cleanup_temp_files',
        'schedule': crontab(hour=4, minute=0),
        'options': {'queue': 'maintenance'},
    },
}

# Celery Task Routes - Route tasks to specific queues
app.conf.task_routes = {
    'apps.notifications.tasks.*': {'queue': 'notifications'},
    'apps.ai.tasks.*': {'queue': 'ai'},
    'apps.analytics.tasks.*': {'queue': 'analytics'},
    'apps.gamification.tasks.*': {'queue': 'gamification'},
    'apps.nft.tasks.*': {'queue': 'blockchain'},
    'apps.moderation.tasks.*': {'queue': 'moderation'},
    'apps.core.tasks.*': {'queue': 'maintenance'},
}

# Celery Task Priorities
app.conf.task_default_priority = 5
app.conf.task_inherit_parent_priority = True

# Task result expiration (7 days)
app.conf.result_expires = 60 * 60 * 24 * 7

# Task compression
app.conf.task_compression = 'gzip'
app.conf.result_compression = 'gzip'

# Error handling
app.conf.task_reject_on_worker_lost = True
app.conf.task_acks_late = True


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    """Debug task to test Celery configuration"""
    print(f'Request: {self.request!r}')


# Custom task base class with error handling
class BaseTask(app.Task):
    """Base task class with retry logic and error handling"""
    
    autoretry_for = (Exception,)
    retry_kwargs = {'max_retries': 3}
    retry_backoff = True
    retry_backoff_max = 600  # 10 minutes
    retry_jitter = True
    
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        """Handle task failure"""
        print(f'Task {self.name} failed: {exc}')
        # You can add Sentry logging or other error handling here
        super().on_failure(exc, task_id, args, kwargs, einfo)
    
    def on_retry(self, exc, task_id, args, kwargs, einfo):
        """Handle task retry"""
        print(f'Task {self.name} retrying: {exc}')
        super().on_retry(exc, task_id, args, kwargs, einfo)
    
    def on_success(self, retval, task_id, args, kwargs):
        """Handle task success"""
        super().on_success(retval, task_id, args, kwargs)


# Set custom base task
app.Task = BaseTask

print("✅ Celery configured successfully")
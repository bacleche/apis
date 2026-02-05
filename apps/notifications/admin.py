from django.contrib import admin
from .models import Notification, NotificationPreference

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'short_message', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('user__username', 'message')
    ordering = ('-created_at',)

    def short_message(self, obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message

    short_message.short_description = "Message"


@admin.register(NotificationPreference)
class NotificationPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'email_notifications', 'push_notifications')

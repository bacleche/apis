from django.contrib import admin
from .models import Follow, Timeline, FeedPost, Share, Mention


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'follower', 'following', 'created_at')
    search_fields = ('follower__username', 'following__username')
    ordering = ('-created_at',)


@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'short_content',
        'created_at',
    )
    search_fields = ('user__username', 'content')
    ordering = ('-created_at',)

    def short_content(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

    short_content.short_description = "Contenu"



@admin.register(FeedPost)
class FeedPostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'short_content',
        'created_at',
    )
    search_fields = ('author__username', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    def short_content(self, obj):
        return obj.content[:60] + '...' if len(obj.content) > 60 else obj.content

    short_content.short_description = "Post"


@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'post',
        'created_at',
    )
    search_fields = ('user__username', 'post__author__username')
    ordering = ('-created_at',)

@admin.register(Mention)
class MentionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'post',
        'created_at',
    )
    search_fields = ('user__username',)
    ordering = ('-created_at',)

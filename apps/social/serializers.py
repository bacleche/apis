from rest_framework import serializers
from .models import Timeline, Follow, FeedPost, Share, Mention


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'created_at']


class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = ['id', 'user', 'content', 'created_at']


class FeedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedPost
        fields = ['id', 'author', 'content', 'created_at']


class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = ['id', 'user', 'post', 'created_at']


class MentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mention
        fields = ['id', 'user', 'post', 'created_at']

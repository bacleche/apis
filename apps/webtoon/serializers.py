from rest_framework import serializers
from .models import Webtoon, Episode, Panel, Rating, Bookmark
from apps.users.models import User


class PanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panel
        fields = ['id', 'episode', 'image', 'order']


class EpisodeSerializer(serializers.ModelSerializer):
    panels = PanelSerializer(many=True, read_only=True)

    class Meta:
        model = Episode
        fields = ['id', 'webtoon', 'title', 'order', 'panels']


class WebtoonSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, read_only=True)
    creator_username = serializers.CharField(source='creator.username', read_only=True)

    class Meta:
        model = Webtoon
        fields = ['id', 'title', 'creator', 'creator_username', 'cover', 'rating', 'episodes']


class RatingSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Rating
        fields = ['id', 'user', 'user_username', 'webtoon', 'score']


class BookmarkSerializer(serializers.ModelSerializer):
    webtoon_title = serializers.CharField(source='webtoon.title', read_only=True)
    episode_title = serializers.CharField(source='episode.title', read_only=True)

    class Meta:
        model = Bookmark
        fields = ['id', 'user', 'webtoon', 'webtoon_title', 'episode', 'episode_title']

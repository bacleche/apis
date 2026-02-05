from rest_framework import serializers
from .models import UserManga, UserWebtoon, Fanfiction, Fanart

class UserMangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserManga
        fields = ['id', 'user', 'title', 'description', 'cover', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

class UserWebtoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWebtoon
        fields = ['id', 'user', 'title', 'description', 'cover', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

class FanfictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fanfiction
        fields = ['id', 'user', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

class FanartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fanart
        fields = ['id', 'user', 'title', 'image', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

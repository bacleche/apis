from rest_framework import serializers
from .models import Manga, Chapter, Page

class MangaSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Manga
        fields = ['id', 'title', 'author', 'description', 'cover', 'status', 'rating', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at', 'rating']

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'manga', 'title', 'order', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'chapter', 'image', 'order', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

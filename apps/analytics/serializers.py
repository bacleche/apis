from rest_framework import serializers
from .models import UserActivity, ReadingStats, Engagement

class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = '__all__'
        read_only_fields = ['user']

class ReadingStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingStats
        fields = '__all__'
        read_only_fields = ['user']

class EngagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engagement
        fields = '__all__'
        read_only_fields = ['user']

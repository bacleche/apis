from rest_framework import serializers
from .models import Recommendation, UserPreference, MoodProfile

class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'
        read_only_fields = ['user']

class UserPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreference
        fields = '__all__'
        read_only_fields = ['user']

class MoodProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodProfile
        fields = '__all__'
        read_only_fields = ['user']

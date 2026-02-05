from rest_framework import serializers
from .models import User, Profile, Badge, Level, Achievement


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'preferences']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'xp', 'level', 'profile'
        ]
        read_only_fields = ['xp', 'level']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ['id', 'name', 'description', 'icon']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['id', 'level_number', 'required_xp']


class AchievementSerializer(serializers.ModelSerializer):
    badge = BadgeSerializer(read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Achievement
        fields = ['id', 'user', 'user_username', 'badge', 'date_earned']

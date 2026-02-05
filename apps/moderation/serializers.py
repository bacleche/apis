from rest_framework import serializers
from .models import Report, Flag, Ban, Warning

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = ['reporter', 'status']


class FlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flag
        fields = '__all__'
        read_only_fields = ['user', 'resolved']


class BanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ban
        fields = '__all__'
        read_only_fields = ['active']


class WarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warning
        fields = '__all__'
        read_only_fields = ['acknowledged']

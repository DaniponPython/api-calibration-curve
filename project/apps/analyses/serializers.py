from rest_framework import serializers

from project.apps.analyses.models import Analysis

class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = '__all__'
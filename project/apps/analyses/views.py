from rest_framework import viewsets
from project.apps.analyses.models import Analysis
from project.apps.analyses.serializers import AnalysisSerializer

class AnalysisViewSet(viewsets.ModelViewSet):
    queryset = Analysis.objects.all().order_by("-id")
    serializer_class = AnalysisSerializer
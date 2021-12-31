from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from project.apps.analyses.models import Analysis
from project.apps.analyses.serializers import AnalysisSerializer
from . import logger


class AnalysisViewSet(viewsets.ModelViewSet):
    serializer_class = AnalysisSerializer
    queryset = Analysis.objects.all().order_by("-id")

    def create(self, request, *args, **kwargs):
        response = super(AnalysisViewSet, self).create(
            request, *args, **kwargs
        )
        response_data = response.data
        logger.info(
            "[AnalysisViewSet] Analysis created with id={} and user={}".format(
                response_data["id"], response_data["analyst"]
            )
        )
        return response

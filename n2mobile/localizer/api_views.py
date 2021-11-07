from rest_framework import viewsets
from rest_framework_gis import filters

from .models import Point
from .serializers import PointSerializer


class PointViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Point.objects.all()
    serializer_class = PointSerializer
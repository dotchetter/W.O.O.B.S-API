
from rest_framework import viewsets
from .models import DeviceReading
from .serializers import DeviceReadingSerializer
from django_filters.rest_framework import DjangoFilterBackend


class DeviceReadingViewSet(viewsets.ModelViewSet):
    queryset = DeviceReading.objects.all()
    serializer_class = DeviceReadingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('device_id', 'temp', 'ph', 'date_time')
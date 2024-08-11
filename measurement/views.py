from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer

class SensorListSerializer(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorRetUpSerializer(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreateSerializer(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
from django.urls import path
from django.contrib import admin
from measurement.views import SensorListSerializer, SensorRetUpSerializer, MeasurementCreateSerializer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', SensorListSerializer.as_view()),
    path('sensors/<int:pk>/', SensorRetUpSerializer.as_view()),
    path('measurements/', MeasurementCreateSerializer.as_view())
]
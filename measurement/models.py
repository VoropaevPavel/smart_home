from django.db import models
# from django.db.models import ImageField


class Sensor(models.Model):
    """Датчик."""
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')


    def __str__(self):
        return self.name


class Measurement(models.Model):
    """Измерение."""
    id = models.BigAutoField(primary_key=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name='Датчик', related_name='measurements')
    temperature = models.FloatField(verbose_name='Значение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    # image = models.ImageField(max_length=100, allow_empty_file=True, use_url=False, verbose_name='Снимки')
    image = models.ImageField(null=True, blank=True, verbose_name='Снимки')


    def __str__(self):
        return f'{self.sensor.name} - {self.temperature}'
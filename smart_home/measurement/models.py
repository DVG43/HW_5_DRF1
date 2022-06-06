from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    desccription = models.TextField(verbose_name='Описание')
    #measurement = models.ForeignKey('Measurement', on_delete=models.CASCADE, related_name='sensors', verbose_name='показания',)
    def __str__(self):
        return self.title


class Measurement(models.Model):
    temperature = models.FloatField(default=0, verbose_name='температура в градусах')
    creating = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Дата измерения')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measures')



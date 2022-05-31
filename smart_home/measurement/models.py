from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    desccription = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class Measurement(models.Model):
    temperature = models.FloatField()
    creating = models.DateTimeField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measures')



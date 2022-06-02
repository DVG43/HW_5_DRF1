from rest_framework import serializers
from models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы

 class MeasurementSerializer(serializers.ModelSerializer):
     class Meta:
         model = Measurement
         fields = ['temperature', 'creating']


 class SensorSerializer(serializers.ModelSerializer):
     measures = MeasurementSerializer(read_only=True,many=True)
     class Meta:
        model = Sensor
        fields = ['id', 'name', 'desccription', 'measures']

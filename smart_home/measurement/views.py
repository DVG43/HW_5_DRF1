# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView,UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorSerializer


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensoridView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorcreatView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorupdateView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MesurcreatView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

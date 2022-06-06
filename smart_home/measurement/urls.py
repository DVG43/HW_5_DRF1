from django.contrib import admin
from django.urls import path

from .views import SensorcreatView, SensorupdateView, MesurcreatView, SensorsView, SensoridView


urlpatterns = [
     path('admin/', admin.site.urls),
     path('create_sensor/', SensorcreatView.as_view()),
     path('update_sensor/<pk>/', SensorupdateView.as_view()),
     path('create_mesuring/', MesurcreatView.as_view()),
     path('sensors/', SensorsView.as_view()),
     path('sensors/<pk>/', SensoridView.as_view()),
]

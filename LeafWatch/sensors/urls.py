from django.urls import path
from . import views

urlpatterns = [
    path('', views.allSensors),
    path('<str:GroupSensor_name>/', views.data),
    path('chartTest', views.chartTest, name="chart-test")
]

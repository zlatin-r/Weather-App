from django.urls import path, include

from weather_app.main_app import views
from weather_app.main_app.views import index

urlpatterns = (
    path('', index),
)
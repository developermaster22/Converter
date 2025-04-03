from django.urls import path
from .views import convertidor_unidades

urlpatterns = [
    path('', convertidor_unidades, name='convertidor_unidades'),
]

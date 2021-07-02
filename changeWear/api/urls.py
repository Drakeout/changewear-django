from django.urls import path
from django.urls.conf import re_path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

# Url vemos endpoint de la api
urlpatterns = [
    path('productos/', productos_ser),
    path('categoria/<pk>', categoria_producto, name='categoria_producto'),
]
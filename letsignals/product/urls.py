from django.urls import path
from . views import *

urlpatterns = [
    path('', product, name='product'),
]

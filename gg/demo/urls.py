from django.urls import path
from .views import *

urlpatterns = [
    path(r'', login, name='login'),
]
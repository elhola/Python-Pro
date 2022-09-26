from django.urls import path, include
from .views import *

app_name = 'mainpage'


urlpatterns = [
    path('', mainpage_view),
]

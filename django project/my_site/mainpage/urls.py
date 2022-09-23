from django.urls import path, include
from .views import *

urlpatterns = [
    path('About/', about_case),
    path('WhyUs/', whyus_case),
    path('Menu/', menu_case),
    path('Specials/', specials_case),
    path('Events/', events_case),
]

from django.urls import path

from sisys.home_app.views import show_home

urlpatterns = (
    path('', show_home, name='home'),
)

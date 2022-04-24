from sisys.home_app.views import show_home
from django.urls import path

urlpatterns = (
    path('', show_home, name='home'),
)


from django.urls import path

from sisys.home_app.views import show_home, show_gallery

urlpatterns = (
    path('', show_home, name='home'),
    path('gallery/', show_gallery, name='gallery'),
)

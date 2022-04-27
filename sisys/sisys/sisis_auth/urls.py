from django.urls import path

from sisys.sisis_auth.views import profile_details, logout_user, login_user, register

urlpatterns = (
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile_details, name='profile details'),
)

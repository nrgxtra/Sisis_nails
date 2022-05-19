from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView

UserModel = get_user_model()


def show_home(request):
    user = request.user.id
    context = {
        'user': user,
    }
    return render(request, 'index.html', context)


def show_gallery(request):
    return render(request, 'gallery-1.html')

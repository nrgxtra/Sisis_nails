from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required

from sisys.sisis_auth.forms import RegisterForm, LoginForm, ProfileForm
from sisys.sisis_auth.models import Profile


def register(request):
    user = request.user
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile details')
    else:
        form = RegisterForm()
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'register.html', context)


def login_user(request):
    user = request.user
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
        'user': request.user,
    }
    return render(request, 'my-account.html', context)

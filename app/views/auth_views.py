from django.http import HttpResponse
from django.shortcuts import redirect, render
from app.forms import LoginForm, SiginForm
from app.models import User
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(request.POST)
    if form.is_valid():
        token = form.cleaned_data['token']
        user = authenticate(request, token=token)
        if user is not None:
            login(request, user)
            return HttpResponse("aaaa")
        else:
            form.add_error('token', 'Invalid token')


def signin(request):
    if request.method == 'GET':
        form = SiginForm()
        return render(request, 'new_user.html', {'form': form})

    form = SiginForm(request.POST)
    if form.is_valid():
        token = form.cleaned_data['alias']
        user = User.objects.create_user(token)
        user.save()
        return HttpResponse(user.token)


def user_logout(request):
    logout(request)
    return HttpResponse("logout")

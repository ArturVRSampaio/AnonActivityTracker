from django.shortcuts import redirect, render
from app.forms import LoginForm, signinForm
from app.models import User
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token']
            user = authenticate(request, token=token)
            if user is not None:
                login(request, user)
                return redirect('groups')
            else:
                form.add_error('token', 'Invalid token')

    form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = signinForm(request.POST)
        if form.is_valid():
            alias = form.cleaned_data['alias']
            user = User.objects.create_user(alias)
            user.save()
            login(request, user)
            return render(request, 'auth/signinResponse.html', {'user': user})
    form = signinForm()
    return render(request, 'auth/signin.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect("index")

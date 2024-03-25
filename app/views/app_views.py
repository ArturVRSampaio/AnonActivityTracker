from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


@login_required
def groups(request):
    user = request.user
    return render(request, 'groups.html', {'user': user})


@login_required
def group(request):
    return render(request, 'group.html')


@login_required
def newGroup(request):
    return render(request, 'newGroup.html')


@login_required
def newEntry(request):
    return render(request, 'newEntry.html')


@login_required
def newActivityType(request):
    return render(request, 'newActivityType.html')

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def groups(request):
    return render(request, 'groups.html')


def group(request):
    return render(request, 'group.html')


def newGroup(request):
    return render(request, 'newGroup.html')


def newEntry(request):
    return render(request, 'newEntry.html')


def newActivityType(request):
    return render(request, 'newActivityType.html')

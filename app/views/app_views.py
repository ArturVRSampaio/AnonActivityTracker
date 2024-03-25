from django.http import HttpResponse


def index(request):
    return HttpResponse("index")


def groups(request):
    return HttpResponse("index")


def group(request):
    return HttpResponse("index")


def newGroup(request):
    return HttpResponse("new group")


def newEntry(request):
    return HttpResponse("new entry")


def newActivityType(request):
    return HttpResponse("new activity")

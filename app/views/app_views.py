from django.http import HttpResponse


def index(request):
    return HttpResponse("index")


def newGroup(request):
    return HttpResponse("new group")


def newActivityType(request):
    return HttpResponse("new activity")


def newEntry(request):
    return HttpResponse("new entry")

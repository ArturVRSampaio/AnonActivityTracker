from django.http import HttpResponse
def index(request):
    return HttpResponse("index")

def newEntry(request):
    return HttpResponse("login")

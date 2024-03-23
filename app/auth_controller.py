from django.http import HttpResponse
from app.models import User
def index(request):
    return HttpResponse("index")


def login(request):
    return HttpResponse("login")


def signin(request):
    user = User.objects.create_user("example")
    user.save()
    return HttpResponse(user)

def logout(request):
    return HttpResponse("logout")

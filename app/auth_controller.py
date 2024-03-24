from django.http import HttpResponse
from app.models import User
from django.contrib.auth import authenticate, login, logout
def index(request):
    return HttpResponse("index")


def user_login(request):
    # if request.method == 'POST':
    # token = request.POST.get('token')
    token = '59ba7e99-fffa-44cb-a9f6-fd8f84676c7d'
    user = authenticate(request, token=token)
    if user is not None:
        login(request, user)
        return HttpResponse(user)
    else:
        return HttpResponse("error")
    # else:
    #     return HttpResponse("error")
    # return



def signin(request):
    user = User.objects.create_user("example")
    user.save()
    return HttpResponse(user.token)

def user_logout(request):
    logout(request)
    return HttpResponse("logout")

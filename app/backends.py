from django.contrib.auth.backends import BaseBackend
from .models import User


class TokenAuthBackend(BaseBackend):
    def authenticate(self, request, token=None):
        try:
            user = User.objects.get(token=token)
            return user
        except :
            return None

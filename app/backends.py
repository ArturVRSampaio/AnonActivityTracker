from django.contrib.auth.backends import BaseBackend
from .models import User


class TokenAuthBackend(BaseBackend):
    def authenticate(self, request, token=None):
        try:
            user = User.objects.get(token=token)
            return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
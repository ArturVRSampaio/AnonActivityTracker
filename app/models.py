from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import uuid
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, alias):
        user = self.model()
        user.alias = alias
        user.token = uuid.uuid4()
        user.set_unusable_password()
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    alias = models.CharField()  # name defined by the user
    token = models.CharField()  # random access key
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'key'
    REQUIRED_FIELDS = [alias, token]

    objects = UserManager()

    def get_full_name(self):
        return self.alias

    def get_short_name(self):
        return self.alias

    def __str__(self):
        return self.alias


class ActivityType(models.Model):
    name = models.CharField()


class Group(models.Model):
    name = models.CharField()
    description = models.CharField()
    owners = models.ManyToManyField(User)


class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activityType = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField()

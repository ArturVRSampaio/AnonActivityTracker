from django.urls import path
from . import auth_controller, app_controller

urlpatterns = [
    path("", auth_controller.index, name="index"),
    path("login", auth_controller.user_login, name="user_login"),
    path("signin", auth_controller.signin, name="signin"),
    path("logout", auth_controller.user_logout, name="user_logout"),

    path("tracker", app_controller.index, name="tracker_index"),
    path("tracker/new", app_controller.newEntry, name="tracker_new"),

    path("group/new", app_controller.newGroup, name="group_new"),
    path("activity_type/new", app_controller.newActivityType, name="activity_type_new"),
]
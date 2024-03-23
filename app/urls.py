from django.urls import path
from . import auth_controller, tracker_controller

urlpatterns = [
    path("", auth_controller.index, name="index"),
    path("login", auth_controller.login, name="login"),
    path("signin", auth_controller.signin, name="signin"),
    path("logout", auth_controller.logout, name="logout"),

    path("/tracker", tracker_controller.index, name="tracker_index"),
    path("/tracker/new", tracker_controller.newEntry, name="tracker_new"),
]
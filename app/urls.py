from django.urls import path

from app.views import auth_views, app_views

urlpatterns = [
    path("", auth_views.index, name="index"),
    path("login", auth_views.user_login, name="user_login"),
    path("signin", auth_views.signin, name="signin"),
    path("logout", auth_views.user_logout, name="user_logout"),

    path("tracker", app_views.index, name="tracker_index"),
    path("tracker/new", app_views.newEntry, name="tracker_new"),

    path("group/new", app_views.newGroup, name="group_new"),
    path("activity_type/new", app_views.newActivityType, name="activity_type_new"),
]
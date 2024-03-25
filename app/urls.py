from django.urls import path

from app.views import auth_views, app_views

urlpatterns = [
    path("", app_views.index, name="index"),

    path("login", auth_views.user_login, name="user_login"),
    path("signin", auth_views.signin, name="signin"),
    path("logout", auth_views.user_logout, name="user_logout"),

    path("groups", app_views.groups, name="groups"),
    path("group/<int:group_id>/", app_views.group, name="group"),
    path("new/entry", app_views.newEntry, name="newEntry"),

    path("group/new", app_views.newGroup, name="group_new"),
    path("activity_type/new", app_views.newActivityType, name="activity_type_new"),
]

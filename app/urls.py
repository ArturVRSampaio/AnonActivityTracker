from django.conf.urls.static import static
from django.urls import path

from AnonActivityTracker import settings
from app.views import auth_views, app_views

urlpatterns = [
    path("", app_views.index, name="index"),

    path("login", auth_views.user_login, name="user_login"),
    path("signin", auth_views.signin, name="signin"),
    path("logout", auth_views.user_logout, name="user_logout"),

    path("groups", app_views.groups, name="groups"),
    path("join/group", app_views.join_group, name="join_group"),
    path("group/<int:group_id>/", app_views.group, name="group"),
    path("new/entry/<int:group_id>/", app_views.new_entry, name="new_entry"),

    path("group/new", app_views.new_group, name="new_group"),
    path("activity_type/new/<int:group_id>/", app_views.new_activity_type, name="new_activity_type"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

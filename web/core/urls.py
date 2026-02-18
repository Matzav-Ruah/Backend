from django.contrib import admin
from django.urls import path
from users.api import api as users_api
from events.api import api as events_api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", users_api.urls),
    path("api/events/", events_api.urls),
]

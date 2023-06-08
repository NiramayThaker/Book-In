from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("signup", views.sign_up, name="sign-up"),
    path("RegisterEvent", views.event_reg, name="event-reg"),
    path("AllEvents", views.view_events, name="all-events"),
    path("", include("django.contrib.auth.urls")),
]

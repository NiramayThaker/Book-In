from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("signup", views.sign_up, name="sign-up"),
    path("", include("django.contrib.auth.urls")),
]


from django.urls import path
from . import views

urlpatterns = [
	path("", views.cric_home, name="cric-home")
]

from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def home(request):
	return render(request, "base/home.html")


def sign_up(request):
	form = RegistrationForm()

	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)

	context = {"form": form}
	return render(request, "registration/signup.html", context=context)

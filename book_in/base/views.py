from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import UserType


# Create your views here.
def home(request):
	user = User.objects.get(id=request.user.id)
	is_venue_user = UserType.objects.get(user=user)

	context = {"user_type": is_venue_user}
	return render(request, "base/home.html", context=context)


def sign_up(request):
	form = RegistrationForm()

	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)

		return redirect('home')

	context = {"form": form}
	return render(request, "registration/signup.html", context=context)

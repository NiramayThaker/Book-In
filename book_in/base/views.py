from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserType


# Create your views here.
@login_required(login_url="login")
def home(request):
	user = User.objects.get(id=request.user.id)
	is_venue_user = UserType.objects.get(user=user)
	

	context = {"user_type": is_venue_user}
	return render(request, "base/home.html", context=context)


def sign_up(request):
	form = RegistrationForm()

	if request.method == "POST":
		form = RegistrationForm(request.POST)
		is_venue = request.POST.get('is_venue_user')
		username = request.POST.get('username')
		if is_venue == "on":
			is_venue = "True"
		else:
			is_venue = "False"

		if form.is_valid():
			try:
				user = form.save()
				username = User.objects.get(username=username)
				user_type, = UserType.objects.create(user=username, venue_user=is_venue)
				user_type.save()
				login(request, user)
			except:
				pass

		return redirect('home')

	context = {"form": form}
	return render(request, "registration/signup.html", context=context)


def event_reg(request):
	return render(request, "base/event_reg.html")

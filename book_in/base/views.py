from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm, EventRegsitrationForm, UserEventBookingForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserType, EventBooking
from datetime import date, datetime, timedelta


# Create your views here.
@login_required(login_url="login")
def home(request):
	user = User.objects.get(id=request.user.id)
	is_venue_user = UserType.objects.get(user=user)
	curr_date = date.today()
	today = datetime.now()
	tomm = today + timedelta(1)
	tomm = tomm.strftime("%D:%M:%Y")
	events = EventBooking.objects.all()


	context = {"user_type": is_venue_user, "events": events, "curr_date": curr_date, "tomm": tomm}
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
	form = EventRegsitrationForm()

	if request.method == "POST":
		form = EventRegsitrationForm(request.POST)
		if form.is_valid:
			event = form.save(commit=False)
			event.event_org = request.user
			event.save()

			return redirect("/")

	context = {"form": form}
	return render(request, "base/event_reg.html", context=context)


def view_events(request):
	events = EventBooking.objects.all()
	curr_date = date.today()

	context = {"events": events, "curr_date": curr_date}
	return render(request, "base/all_events.html", context=context)


def book_event(request):
	form = UserEventBookingForm()

	context = {'form': form}
	return render(request, "base/user_booking.html", context=context)


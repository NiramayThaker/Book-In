from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import EventBooking


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=False)
	is_venue_user = forms.BooleanField(required=False)

	class Meta:
		model = User
		fields = ["username", "email", "is_venue_user", "password1", "password2"]


class EventRegsitrationForm(forms.ModelForm):
	class Meta:
		model = EventBooking
		fields = "__all__"
		exclude = ['event_org']

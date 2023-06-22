from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserType(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	venue_user = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.user} - {self.venue_user}"


class EventBooking(models.Model):
	event_org = models.ForeignKey(User, on_delete=models.CASCADE)
	event = models.CharField(max_length=50)
	date = models.DateField()
	starting_time = models.TimeField()
	ending_time = models.TimeField()
	pass_price = models.FloatField()
	place = models.TextField()

	def __str__(self) -> str:
		return f"{self.event}, by {self.event_org}, at {self.date}"


class UserEventBooking(models.Model):
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	event = models.ForeignKey(EventBooking, on_delete=models.CASCADE)


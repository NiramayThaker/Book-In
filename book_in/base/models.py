from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserType(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	venue_user = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.user} - {self.venue_user}"

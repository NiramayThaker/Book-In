from django.contrib import admin
from .models import UserType, EventBooking

# Register your models here.
admin.site.register(UserType)
admin.site.register(EventBooking)

from django.contrib import admin
from .models import UserType, EventBooking, UserEventBooking

# Register your models here.
admin.site.register(UserType)
admin.site.register(EventBooking)
admin.site.register(UserEventBooking)

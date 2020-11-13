from django.contrib import admin

from app_calendar.models import User, Country, Event, Holiday

admin.site.register(User)
admin.site.register(Country)
admin.site.register(Event)
admin.site.register(Holiday)


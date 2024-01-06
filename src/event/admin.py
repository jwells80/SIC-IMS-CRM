from django.contrib import admin
from .models import (
    Event,
    EventTimeSlot,
    EventCheckIn,
    AttendeeCheckOut,
    VolunteerTime,
)


admin.site.register(VolunteerTime)


class EventTimeSlotInline(admin.TabularInline):
    model = EventTimeSlot


class EventCheckInInline(admin.TabularInline):
    model = EventCheckIn


class AttendeeCheckOutInline(admin.TabularInline):
    model = AttendeeCheckOut


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventTimeSlotInline, EventCheckInInline, AttendeeCheckOutInline]

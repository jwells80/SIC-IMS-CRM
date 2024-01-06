from django.contrib import admin
from .models import (
    Attendee,
    AttendeeSignup,
    Volunteer,
    VolunteerAgreement,
    VolunteerSignup,
)
from event.models import VolunteerTime, AttendeeCheckOut


class AttendeeSignupInline(admin.TabularInline):
    model = AttendeeSignup
    extra = 0


class VolunteerSignupInline(admin.TabularInline):
    model = VolunteerSignup
    extra = 0
    verbose_name = "Volunteer Signup"


class VolunteerAgreementInline(admin.TabularInline):
    model = VolunteerAgreement
    extra = 0


class AttendeeCheckOutInline(admin.StackedInline):
    model = AttendeeCheckOut
    extra = 0


class VolunteerTimeInline(admin.TabularInline):
    model = VolunteerTime
    extra = 0


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    inlines = [VolunteerSignupInline, VolunteerTimeInline, VolunteerAgreementInline]


@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    inlines = [AttendeeCheckOutInline, AttendeeSignupInline]

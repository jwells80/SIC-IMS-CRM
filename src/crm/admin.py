from django.contrib import admin
from .models import (
    Attendee,
    AttendeeSignup,
    Volunteer,
    VolunteerAgreement,
    VolunteerSignup,
    AttendeeAgreement,
    AgreementPart,
    Agreement,
)
from event.models import VolunteerTime, AttendeeCheckOut
from django.contrib.admin.sites import AdminSite
from unfold.admin import ModelAdmin


class AttendeeAgreementInline(admin.TabularInline):
    model = AttendeeAgreement
    extra = 0


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


@admin.register(AgreementPart)
class AgreementPartAdmin(ModelAdmin):
    ...


@admin.register(Agreement)
class AgreementAdmin(ModelAdmin):
    # inlines = [AgreementPartsInline]
    ...


@admin.register(Volunteer)
class VolunteerAdmin(ModelAdmin):
    inlines = [VolunteerSignupInline, VolunteerTimeInline, VolunteerAgreementInline]


@admin.register(Attendee)
class AttendeeAdmin(ModelAdmin):
    inlines = [AttendeeCheckOutInline, AttendeeSignupInline]


AdminSite.site_title = "Sisters in Christ"
AdminSite.site_header = "Sisters in Christ"
AdminSite.index_title = "Sisters in Christ Inventory Admin"

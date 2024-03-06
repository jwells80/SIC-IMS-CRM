from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = "crm/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home"
        return context


class VolunteerView(TemplateView):
    template_name = "crm/volunteer.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Volunteer"
        return context


class AttendeeView(TemplateView):
    template_name = "crm/attendee.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Attendee"
        return context


class AttendeeAgreementView(TemplateView):
    template_name = "crm/attendee_agreement.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Attendee Agreement"
        return context


class AttendeeSignupView(TemplateView):
    template_name = "crm/attendee_signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Attendee Signup"
        return context

from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Item

# Create your views here.


class CheckOutView(TemplateView):
    template_name = "inventory/check_out.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = Item.objects.all()
        return context


class AddItemView(TemplateView):
    template_name = "inventory/snippet/add_item.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Item"
        return context

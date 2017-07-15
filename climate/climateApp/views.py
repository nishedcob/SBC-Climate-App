from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "pages/index.html"


class DataView(TemplateView):
    template_name = "pages/datos.html"


class GraphView(TemplateView):
    template_name = "pages/graficos.html"

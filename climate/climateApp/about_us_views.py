from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View


class GenericAboutUsView(View):
    template_name = "pages/about_us.html"


class UTPLAboutUsView(GenericAboutUsView):
    context = {
        'title': "Acerca de Nosotros - UTPL",
        'item_1': False,
        'heading_1': None,
        'text_1': None,
        'image_1': None,
        'image_before_text_1': False,
        'item_2': False,
        'heading_2': None,
        'text_2': None,
        'image_2': None,
        'image_before_text_2': False,
        'item_3': False,
        'heading_3': None,
        'text_3': None,
        'image_3': None,
        'image_before_text_3': False
    }

    def get(self, request):
        return render(request, self.template_name, context=self.context)


class SBCAboutUsView(GenericAboutUsView):
    context = {
        'title': "Acerca de Nosotros - Sistemas Basados en el Conocimiento",
        'item_1': False,
        'heading_1': None,
        'text_1': None,
        'image_1': None,
        'image_before_text_1': False,
        'item_2': False,
        'heading_2': None,
        'text_2': None,
        'image_2': None,
        'image_before_text_2': False,
        'item_3': False,
        'heading_3': None,
        'text_3': None,
        'image_3': None,
        'image_before_text_3': False
    }

    def get(self, request):
        return render(request, self.template_name, context=self.context)


class MADBAAboutUsView(GenericAboutUsView):
    context = {
        'title': "Acerca de Nosotros - Marcelo Bravo",
        'item_1': False,
        'heading_1': None,
        'text_1': None,
        'image_1': None,
        'image_before_text_1': False,
        'item_2': False,
        'heading_2': None,
        'text_2': None,
        'image_2': None,
        'image_before_text_2': False,
        'item_3': False,
        'heading_3': None,
        'text_3': None,
        'image_3': None,
        'image_before_text_3': False
    }

    def get(self, request):
        return render(request, self.template_name, context=self.context)


class NSEDAboutUsView(GenericAboutUsView):
    context = {
        'title': "Acerca de Nosotros - Nicholas Earley",
        'item_1': False,
        'heading_1': None,
        'text_1': None,
        'image_1': None,
        'image_before_text_1': False,
        'item_2': False,
        'heading_2': None,
        'text_2': None,
        'image_2': None,
        'image_before_text_2': False,
        'item_3': False,
        'heading_3': None,
        'text_3': None,
        'image_3': None,
        'image_before_text_3': False
    }

    def get(self, request):
        return render(request, self.template_name, context=self.context)

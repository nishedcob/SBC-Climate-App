from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from sparqlApp import sparql
from climate import settings

# Create your views here.

from django.views.generic import TemplateView
from django.views import View

class HomeView(TemplateView):
    template_name = "pages/index.html"


class DataView(TemplateView):
    template_name = "pages/datos.html"


class GraphView(TemplateView):
    template_name = "pages/graficos.html"


class VocabDefView(TemplateView):
    template_name = "pages/vocab.html"


class RDFView(View):

    def get(self, request):
        query = """
        SELECT ?s ?o ?p
        FROM <%s>
        WHERE {
          ?s ?p ?o
        }
        """ % settings.SPARQL_SETTINGS['default']['vocab-graph-uri']
        data = sparql.sparql_query(query)
        return JsonResponse(data)

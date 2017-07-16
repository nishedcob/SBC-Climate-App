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


class BruteContaminationGraphView(View):
    template_name = "pages/grafico_contaminacion_bruta.html"

    def get(self, request):
        query = """
        SELECT ?country ?year ?data
        FROM <http://localhost:8890/climate>
        WHERE {
        ?s <http://climate.utpl.edu.ec/vocab/belongsToDataSeries> <http://climate.utpl.edu.ec/data/EN.ATM.CO2E.KT> .
        ?s <http://climate.utpl.edu.ec/vocab/country> ?c .
        ?s <http://climate.utpl.edu.ec/vocab/dataPoint> ?data .
        ?s <http://climate.utpl.edu.ec/vocab/year> ?y .
        ?c <http://purl.org/dc/terms/title> ?country .
        ?y <http://climate.utpl.edu.ec/vocab/year> ?year .
        } ORDER BY desc(?data)
        """
        data = sparql.sparql_query(query)
        error = False
        if data is None:
            error = True
            data = "Some sort of error occurred..."
        else:
            json_data = data
            header = json_data['head']['vars']
            tmp_data = json_data['results']['bindings']
            # print_data = json.dumps(data, sort_keys=True, indent=4)
            # print(print_data)
            data = []
            for data_point in tmp_data:
                save_data_point = []
                for attr, attr_data in data_point.items():
                    save_data_point.append(attr_data['value'])
                data.append(save_data_point)
        context = {
            'error': error,
            'response': data
        }
        return render(request, self.template_name, context)


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

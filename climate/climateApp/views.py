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


# class BruteContaminationGraphView(View):
#     template_name = "pages/grafico_contaminacion_bruta.html"
#
#     def get(self, request):
#         query = """
#         SELECT ?1 ?2 ?3
#         FROM <http://localhost:8890/climate>
#         WHERE {
#         ?s <http://climate.utpl.edu.ec/vocab/belongsToDataSeries> <http://climate.utpl.edu.ec/data/EN.ATM.CO2E.KT> .
#         ?s <http://climate.utpl.edu.ec/vocab/country> ?c .
#         ?s <http://climate.utpl.edu.ec/vocab/dataPoint> ?3 .
#         ?s <http://climate.utpl.edu.ec/vocab/year> ?y .
#         ?c <http://purl.org/dc/terms/title> ?1 .
#         ?y <http://climate.utpl.edu.ec/vocab/year> ?2 .
#         } ORDER BY desc(?3)
#         """
#         data = sparql.sparql_query(query)
#         error = False
#         if data is None:
#             error = True
#             data = "Some sort of error occurred..."
#         else:
#             json_data = data
#             header = json_data['head']['vars']
#             tmp_data = json_data['results']['bindings']
#             # print_data = json.dumps(data, sort_keys=True, indent=4)
#             # print(print_data)
#             data = []
#             for data_point in tmp_data:
#                 save_data_point = []
#                 for attr, attr_data in sorted(data_point.items()):
#                     save_data_point.append(attr_data['value'])
#                 data.append(save_data_point)
#         context = {
#             'error': error,
#             'response': data
#         }
#         return render(request, self.template_name, context)


# class PerCapitaContaminationGraphView(View):
#     template_name = "pages/grafico_contaminacion_por_cabeza.html"
#
#     def get(self, request):
#         query = """
#         SELECT ?1 ?2 ?3
#         FROM <http://localhost:8890/climate>
#         WHERE {
#         ?s <http://climate.utpl.edu.ec/vocab/belongsToDataSeries> <http://climate.utpl.edu.ec/data/EN.ATM.CO2E.PC> .
#         ?s <http://climate.utpl.edu.ec/vocab/country> ?c .
#         ?s <http://climate.utpl.edu.ec/vocab/dataPoint> ?3 .
#         ?s <http://climate.utpl.edu.ec/vocab/year> ?y .
#         ?c <http://purl.org/dc/terms/title> ?1 .
#         ?y <http://climate.utpl.edu.ec/vocab/year> ?2 .
#         } ORDER BY desc(?3)
#         """
#         data = sparql.sparql_query(query)
#         error = False
#         if data is None:
#             error = True
#             data = "Some sort of error occurred..."
#         else:
#             json_data = data
#             header = json_data['head']['vars']
#             tmp_data = json_data['results']['bindings']
#             # print_data = json.dumps(data, sort_keys=True, indent=4)
#             # print(print_data)
#             data = []
#             for data_point in tmp_data:
#                 save_data_point = []
#                 for attr, attr_data in sorted(data_point.items()):
#                     save_data_point.append(attr_data['value'])
#                 data.append(save_data_point)
#         context = {
#             'error': error,
#             'response': data
#         }
#         return render(request, self.template_name, context)


class GenericLineGraphView(View):
    title = ""
    graph_title = ""
    source = ""
    x_axis = ""
    x_units = None
    y_axis = ""
    y_units = None
    template_name = "pages/grafico_lineal_generica.html"
    query = None

    def build_query(self):
        return self.query

    def get(self, request):
        if not self.build_query():
            return None
        data = sparql.sparql_query(self.build_query())
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
                for attr, attr_data in sorted(data_point.items()):
                    save_data_point.append(attr_data['value'])
                data.append(save_data_point)
        context = {
            'error': error,
            'response': data,
            'title': self.title,
            'graph_title': self.graph_title,
            'source': self.source,
            'x_axis': self.x_axis,
            'x_units': self.x_units,
            'y_axis': self.y_axis,
            'y_units': self.y_units
        }
        return render(request, self.template_name, context)


class GenericIndicatorLineGraphView(GenericLineGraphView):
    query = """
        SELECT ?1 ?2 ?3
        FROM <http://localhost:8890/climate>
        WHERE {
        ?s <http://climate.utpl.edu.ec/vocab/belongsToDataSeries> <http://climate.utpl.edu.ec/data/%s> .
        ?s <http://climate.utpl.edu.ec/vocab/country> ?c .
        ?s <http://climate.utpl.edu.ec/vocab/dataPoint> ?3 .
        ?s <http://climate.utpl.edu.ec/vocab/year> ?y .
        ?c <http://purl.org/dc/terms/title> ?1 .
        ?y <http://climate.utpl.edu.ec/vocab/year> ?2 .
        } ORDER BY desc(?3)
        """
    indicator = ""

    def build_query(self):
        return self.query % self.indicator


class BruteContaminationGraphView(GenericIndicatorLineGraphView):
    title = "Grafico de Contamininacion Bruta"
    graph_title = "Contaminacion Bruta de Paises"
    source = "Banco Mundial"
    x_axis = "Año"
    y_axis = "Emisiones de CO2 (kt)"
    y_units = "kt"
    indicator = "EN.ATM.CO2E.KT"


class PerCapitaContaminationGraphView(GenericIndicatorLineGraphView):
    title = "Grafico de Contamininacion per Capita"
    graph_title = "Contaminacion per Capita"
    source = "Banco Mundial"
    x_axis = "Año"
    y_axis = "Emisiones de CO2 (kt)"
    y_units = "kt"
    indicator = "EN.ATM.CO2E.PC"


class RenewableEnergyProductionGraphView(GenericIndicatorLineGraphView):
    title = "Grafico de Producion de Energia Renovable"
    graph_title = "Produccion de Energia Renovable"
    source = "Banco Mundial"
    x_axis = "Año"
    y_axis = "Porcentaje de Energia Renovable (%)"
    y_units = "%"
    indicator = "EG.ELC.RNEW.ZS"


class RenewableEnergyConsumptionGraphView(GenericIndicatorLineGraphView):
    title = "Grafico de Consumo de Energia Renovable"
    graph_title = "Consumo de Energia Renovable"
    source = "Banco Mundial"
    x_axis = "Año"
    y_axis = "Porcentaje de Energia Renovable (%)"
    y_units = "%"
    indicator = "EG.FEC.RNEW.ZS"


class StatisticsGraphView(View):
    template_name = "pages/grafico_estadisticas.html"

    def get(self, request):
        query_data_count = """
        SELECT count(*) AS ?count
        FROM <http://localhost:8890/climate>
        WHERE {
          ?s ?p ?o.
        }
        """
        data_count = sparql.sparql_query(query_data_count)
        data_error = False
        if data_count is None:
            data_error = True
            data_count = "Some sort of error occurred..."
        else:
            json_data = data_count
            header = json_data['head']['vars']
            tmp_data = json_data['results']['bindings']
            # print_data = json.dumps(data, sort_keys=True, indent=4)
            # print(print_data)
            data_count = []
            for data_point in tmp_data:
                save_data_point = []
                for attr, attr_data in data_point.items():
                    save_data_point.append(attr_data['value'])
                data_count.append(save_data_point)
        query_vocab_count = """
        SELECT count(*) AS ?count
        FROM <http://localhost:8890/climate_vocab>
        WHERE {
          ?s ?p ?o.
        }
        """
        vocab_count = sparql.sparql_query(query_vocab_count)
        vocab_error = False
        if vocab_count is None:
            vocab_error = True
            vocab_count = "Some sort of error occurred..."
        else:
            json_vocab = vocab_count
            header = json_vocab['head']['vars']
            tmp_vocab = json_vocab['results']['bindings']
            # print_vocab = json.dumps(vocab, sort_keys=True, indent=4)
            # print(print_vocab)
            vocab_count = []
            for vocab_point in tmp_vocab:
                save_vocab_point = []
                for attr, attr_vocab in vocab_point.items():
                    save_vocab_point.append(attr_vocab['value'])
                vocab_count.append(save_vocab_point)
        context = {
            'data_error': data_error,
            'vocab_error': vocab_error,
            'data_count': data_count[0][0],
            'vocab_count': vocab_count[0][0]
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

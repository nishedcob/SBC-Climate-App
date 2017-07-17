from django.shortcuts import render

from django.views import View
#from django.views.generic import TemplateView

from . import forms, sparql
from climate import settings

#import json

# Create your views here.


class SPARQL_View(View):
    #template_name = "sparql.html"
    template_name = "pages/sparql.html"

    def get(self, request):
        form = forms.SPARQL_SearchForm()
        context = {
            'form': form,
            'response': None
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = forms.SPARQL_SearchForm(request.POST)
        error = False
        data = None
        header = None
        if form.is_valid():
            graph_uri = form.cleaned_data["graph_uri"]
            if graph_uri is None or graph_uri == "":
                graph_uri = settings.SPARQL_SETTINGS['default']['graph-uri']
            query = form.cleaned_data["query"]
            data = sparql.sparql_query(query, graph_url=graph_uri)
            if data is None:
                error = True
                data = "Some sort of error occurred..."
            else:
                json_data = data
                header = json_data['head']['vars']
                tmp_data = json_data['results']['bindings']
                #print_data = json.dumps(data, sort_keys=True, indent=4)
                #print(print_data)
                data = []
                for data_point in tmp_data:
                    save_data_point = []
                    #print(sorted(data_point.items()))
                    for attr, attr_data in sorted(data_point.items()):
                        save_data_point.append(attr_data['value'])
                    data.append(save_data_point)
                    #print(save_data_point)
        context = {
            'form': form,
            'response': data,
            'error': error,
            'header': header
        }
        #print(data)
        return render(request, self.template_name, context)

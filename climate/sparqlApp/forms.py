
from django import forms


class SPARQL_SearchForm(forms.Form):
    graph_uri = forms.CharField(required=False)
    query = forms.CharField(widget=forms.Textarea, required=True)


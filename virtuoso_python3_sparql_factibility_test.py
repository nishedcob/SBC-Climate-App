import urllib, urllib.request, json

baseURL = "http://localhost:8890/sparql/"
graphURL = "http://localhost:8890/climate"
query = """
SELECT count(*)
FROM <%s>
WHERE {
?s ?p ?o .
}
""" % graphURL
format="application/json"
params={
    "default-graph": "",
    "should-sponge": "soft",
    "query": query,
    "debug": "on",
    "timeout": "",
    "format": format,
    "save": "display",
    "fname": ""
}
querypart = urllib.parse.urlencode(params)
binary_query_part = querypart.encode('ascii')
response = urllib.request.urlopen(baseURL,binary_query_part).read().decode('utf8')
data = json.loads(response)
print(json.dumps(data, sort_keys=True, indent=4))


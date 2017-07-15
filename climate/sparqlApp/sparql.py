import json
import urllib.parse as parse
import urllib.request
import climate.settings as settings


def prepare_query(query, graph_url=settings.SPARQL_SETTINGS['default']['graph-uri']):
    from_clause = settings.SPARQL_FROM_CLAUSE_PATTERN.search(query)
    if from_clause:
        select_clause = settings.SPARQL_SELECT_CLAUSE_PATTERN.search(query)
        where_clause = settings.SPARQL_WHERE_CLAUSE_PATTERN.search(query)
        if select_clause and where_clause:
            return query
        else:
            return None
    else:
        select_clause = settings.SPARQL_SELECT_CLAUSE_PATTERN.search(query)
        where_clause = settings.SPARQL_WHERE_CLAUSE_PATTERN.search(query)
        if select_clause and where_clause:
            from_clause_string = "FROM <%s>" % graph_url
            limit_clause = settings.SPARQL_LIMIT_CLAUSE_PATTERN.search(query)
            if limit_clause:
                return select_clause.group(0) + "\n" + from_clause_string + "\n" + where_clause.group(0) + "\n" +\
                       limit_clause.group(0)
            else:
                return select_clause.group(0) + "\n" + from_clause_string + "\n" + where_clause.group(0)
        else:
            return None


def sparql_query(query, format=settings.SPARQL_SETTINGS['default']['format'],
                 graph_url=settings.SPARQL_SETTINGS['default']['graph-uri'],
                 base_url=settings.SPARQL_SETTINGS['default']['sparql-endpoint']):
    query = prepare_query(query, graph_url)
    #print(query)
    if query:
        params = {
            "default-graph": "",
            "should-sponge": "soft",
            "query": query,
            "debug": "on",
            "timeout": "",
            "format": format,
            "save": "display",
            "fname": ""
        }
        querypart = parse.urlencode(params)
        binary_query_part = querypart.encode('ascii')
        response = urllib.request.urlopen(base_url, binary_query_part).read().decode('utf8')
        return json.loads(response)
    else:
        return None

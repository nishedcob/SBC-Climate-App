# SBC-Climate-App
App Django Climate Data for SBC

## Operating System Environment Requirements
- PostgreSQL and its header files (usually as a -dev on Debian based systems or -devel package on RHEL/Fedora based systems)
- Virtuoso OpenSource Server
- Python 3 with pip and virtualenv

__Suggested platform:__

UNIX based or similar, preferably GNU/Linux like _Debian 8/9_ or _CentOS 7_.

## Setup devstack
1. **Setup Database**:
    ```{Bash}
    # su - postgres
    $ psql
    ```

    Connect to Postgres Database.

    ```{SQL}
    CREATE USER sbcuser WITH PASSWORD 's8cU$3r';
    CREATE DATABASE climatedb WITH OWNER sbcuser;
    ```
    Create database for Climate App.

2. **Setup TripleStore**:

    Navegate to:
    http://localhost:8890/conductor/

    Click on Linked Data then on Quad Store Upload.

    Set the Graph URI as http://localhost:8890/climate

    Choose the RDF Files (one by one from [data](https://gitlab.com/nishedcob/SBC-Data-Translator/tree/master/data) folder, followed by "Upload"), from full_model.nt.00.rdf all the way through full_model.nt.10.rdf.

    To upload the vocabulary, change the Graph URI to http://localhost:8890/climate_vocab and upload vocab.rdf.

    To verify the uploaded data, navegate to http://localhost:8890/sparql and execute the following queries:

    ```{SQL}
    SELECT count(*)
    FROM <http://localhost:8890/climate>
    WHERE {
    ?s ?p ?o .
    }
    ```

    The result should return 2684440.

    ```{SQL}
    SELECT count(*)
    FROM <http://localhost:8890/climate_vocab>
    WHERE {
    ?s ?p ?o .
    }
    ```

    The result should return 251.

3. **Create and Activate Virtual Environment**:
    ```{bash}
    $ source activate.sh
    ```

    From the root of the project.

4. **Migrate Database**:
    ```{bash}
    $ cd climate
    $ python manage.py migrate
    ```

5. **Start Server**:
    ```{bash}
    $ python manage.py runserver
    ```
    Navegate to http://localhost:8000/ .

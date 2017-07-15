su - postgres
psql
CREATE USER "sbcuser" WITH PASSWORD 's8cU$3r';
CREATE DATABASE "climatedb" WITH OWNER "sbcuser"; 
\q
psql -U postgres "climatedb"
CREATE SCHEMA "climateapp" authorization "sbcuser";
ALTER USER "sbcuser" SET search_path TO "climateapp";
\q
psql -U "sbcuser" "climatedb"

select current_schema();

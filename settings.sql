-- settings.sql
CREATE DATABASE grocery;
CREATE USER groceryuser WITH PASSWORD 'grocery';
GRANT ALL PRIVILEGES ON DATABASE grocery TO groceryuser;
-- settings.sql
CREATE DATABASE petpursuit;
CREATE USER petpursuituser WITH PASSWORD 'petpursuit';
GRANT ALL PRIVILEGES ON DATABASE petpursuit TO petpursuituser;
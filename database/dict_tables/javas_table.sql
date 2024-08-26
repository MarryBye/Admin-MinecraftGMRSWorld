DROP TABLE IF EXISTS dict_tables.javas CASCADE;

CREATE TABLE IF NOT EXISTS dict_tables.javas (
    id SERIAL PRIMARY KEY,
    java_version VARCHAR(32),
    java_url VARCHAR(256)
)
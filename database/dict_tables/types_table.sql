DROP TABLE IF EXISTS dict_tables.types CASCADE;

CREATE TABLE IF NOT EXISTS dict_tables.types (
    id SERIAL PRIMARY KEY,
    type_name VARCHAR(16)
)
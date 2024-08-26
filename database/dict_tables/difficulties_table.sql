DROP TABLE IF EXISTS dict_tables.difficulties CASCADE;

CREATE TABLE IF NOT EXISTS dict_tables.difficulties (
    id SERIAL PRIMARY KEY,
    difficulty_name VARCHAR(16)
)
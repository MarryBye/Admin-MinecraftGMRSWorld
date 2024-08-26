DROP TABLE IF EXISTS connect_tables.modpacks_tags CASCADE;

CREATE TABLE IF NOT EXISTS connect_tables.modpacks_tags (
    id SERIAL PRIMARY KEY,
    modpack_id INTEGER REFERENCES data_tables.modpacks(id),
    tag_id INTEGER REFERENCES dict_tables.tags(id)
)
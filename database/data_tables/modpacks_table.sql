DROP TABLE IF EXISTS data_tables.modpacks CASCADE;

CREATE TABLE IF NOT EXISTS data_tables.modpacks (
    id SERIAL PRIMARY KEY,
    modpack_name VARCHAR(64),
    modpack_description VARCHAR(1024),
    modpack_icon VARCHAR(128),
    modpack_url VARCHAR(256),
    modpack_java INTEGER REFERENCES dict_tables.javas(id),
    modpack_type INTEGER REFERENCES dict_tables.types(id),
    modpack_difficulty INTEGER REFERENCES dict_tables.difficulties(id)
)
DROP FUNCTION IF EXISTS get_modpack CASCADE;

CREATE OR REPLACE FUNCTION get_modpack(id_arg INTEGER) 
RETURNS Table(
    id INTEGER,
    modpack_name VARCHAR(64),
    modpack_description VARCHAR(1024),
    modpack_icon VARCHAR(128),
    modpack_url VARCHAR(256),
    modpack_java INTEGER,
    modpack_type INTEGER,
    modpack_difficulty INTEGER
) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM data_tables.modpacks as modpacks
    WHERE modpacks.id = id_arg;
END;
$$ LANGUAGE plpgsql;
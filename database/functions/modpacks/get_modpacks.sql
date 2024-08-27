DROP FUNCTION IF EXISTS get_modpacks CASCADE;

CREATE OR REPLACE FUNCTION get_modpacks() 
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
    SELECT * FROM data_tables.modpacks;
END;
$$ LANGUAGE plpgsql;
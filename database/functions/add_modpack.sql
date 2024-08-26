DROP FUNCTION IF EXISTS add_modpack CASCADE;

CREATE OR REPLACE FUNCTION add_modpack(
    modpack_name VARCHAR(16),
    modpack_description VARCHAR(1024),
    modpack_icon VARCHAR(128),
    modpack_url VARCHAR(256),
    modpack_java INTEGER,
    modpack_type INTEGER,
    modpack_difficulty INTEGER
) 
RETURNS VOID AS $$
BEGIN
    INSERT INTO data_tables.modpacks(
        data_tables.modpacks.modpack_name,
        data_tables.modpacks.modpack_description,
        data_tables.modpacks.modpack_icon,
        data_tables.modpacks.modpack_url,
        data_tables.modpacks.modpack_java,
        data_tables.modpacks.modpack_type,
        data_tables.modpacks.modpack_difficulty
    ) VALUES (
        modpack_name,
        modpack_description,
        modpack_icon,
        modpack_url,
        modpack_java,
        modpack_type,
        modpack_difficulty
    );
END;
$$ LANGUAGE plpgsql;
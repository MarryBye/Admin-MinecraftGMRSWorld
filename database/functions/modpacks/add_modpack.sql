DROP FUNCTION IF EXISTS add_modpack CASCADE;

CREATE OR REPLACE FUNCTION add_modpack(
    modpack_name_arg VARCHAR(64),
    modpack_description_arg VARCHAR(1024),
    modpack_icon_arg VARCHAR(128),
    modpack_url_arg VARCHAR(256),
    modpack_java_arg INTEGER,
    modpack_type_arg INTEGER,
    modpack_difficulty_arg INTEGER
) 
RETURNS VOID AS $$
BEGIN
    INSERT INTO data_tables.modpacks(
        modpack_name,
        modpack_description,
        modpack_icon,
        modpack_url,
        modpack_java,
        modpack_type,
        modpack_difficulty
    ) VALUES (
        modpack_name_arg,
        modpack_description_arg,
        modpack_icon_arg,
        modpack_url_arg,
        modpack_java_arg,
        modpack_type_arg,
        modpack_difficulty_arg
    );
END;
$$ LANGUAGE plpgsql;
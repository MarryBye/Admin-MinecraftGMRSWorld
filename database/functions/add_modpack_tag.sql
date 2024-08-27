DROP FUNCTION IF EXISTS add_modpack_tag CASCADE;

CREATE OR REPLACE FUNCTION add_modpack_tag(
    modpack_id_arg INTEGER,
    tag_id_arg INTEGER
) 
RETURNS VOID AS $$
BEGIN
    INSERT INTO connect_tables.modpacks_tags(
        modpack_id,
        tag_id
    ) VALUES (
        modpack_id_arg,
        tag_id_arg
    );
END;
$$ LANGUAGE plpgsql;
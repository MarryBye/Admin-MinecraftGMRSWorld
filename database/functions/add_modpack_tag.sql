DROP FUNCTION IF EXISTS add_modpack_tag CASCADE;

CREATE OR REPLACE FUNCTION add_modpack_tag(
    modpack_id INTEGER,
    tag_id INTEGER
) 
RETURNS VOID AS $$
BEGIN
    INSERT INTO connect_tables.modpacks_tags(
        connect_tables.modpacks_tags.modpack_id,
        connect_tables.modpacks_tags.tag_id
    ) VALUES (
        modpack_id,
        tag_id
    );
END;
$$ LANGUAGE plpgsql;
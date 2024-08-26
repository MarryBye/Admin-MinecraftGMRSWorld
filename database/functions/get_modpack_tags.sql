DROP FUNCTION IF EXISTS get_modpack_tags CASCADE;

CREATE OR REPLACE FUNCTION get_modpack_tags(modpack_id INTEGER) 
RETURNS Table(
    tag_id INTEGER,
    tag_name VARCHAR(16),
    tag_color VARCHAR(7)
) AS $$
BEGIN
    RETURN QUERY
    SELECT tags.* 
    FROM 
    dict_tables.tags AS tags, 
    connect_tables.modpacks_tags AS modpacks_tags
    WHERE
    modpacks_tags.id = tags.id
    AND
    modpacks_tags.modpack_id = modpack_id;
END;
$$ LANGUAGE plpgsql;
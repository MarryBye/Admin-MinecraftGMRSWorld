DROP FUNCTION IF EXISTS get_tag CASCADE;

CREATE OR REPLACE FUNCTION get_tag(id_arg INTEGER) 
RETURNS Table(
    id INTEGER,
    tag_name VARCHAR(16),
    tag_color VARCHAR(7)
) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM dict_tables.tags as tags
    WHERE tags.id = id_arg;
END;
$$ LANGUAGE plpgsql;
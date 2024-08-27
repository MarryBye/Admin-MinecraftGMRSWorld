DROP FUNCTION IF EXISTS add_tag CASCADE;

CREATE OR REPLACE FUNCTION add_tag(
    tag_name_arg VARCHAR(16),
    tag_color_arg VARCHAR(7)
) 
RETURNS VOID AS $$
BEGIN
    INSERT INTO dict_tables.tags(
        tag_name,
        tag_color
    ) VALUES (
        tag_name_arg,
        tag_color_arg
    );
END;
$$ LANGUAGE plpgsql;
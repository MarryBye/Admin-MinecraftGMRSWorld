DROP FUNCTION IF EXISTS get_type CASCADE;

CREATE OR REPLACE FUNCTION get_type(id_arg INTEGER) 
RETURNS Table(
    id INTEGER,
    type_name VARCHAR(16)
) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM dict_tables.types as types
    WHERE types.id = id_arg;
END;
$$ LANGUAGE plpgsql;
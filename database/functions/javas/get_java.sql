DROP FUNCTION IF EXISTS get_java CASCADE;

CREATE OR REPLACE FUNCTION get_java(id_arg INTEGER) 
RETURNS Table(
    id INTEGER,
    java_version VARCHAR(32),
    java_url VARCHAR(256)
) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM dict_tables.javas as javas
    WHERE javas.id = id_arg;
END;
$$ LANGUAGE plpgsql;
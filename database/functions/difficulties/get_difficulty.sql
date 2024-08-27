DROP FUNCTION IF EXISTS get_difficulty CASCADE;

CREATE OR REPLACE FUNCTION get_difficulty(id_arg INTEGER) 
RETURNS Table(
    id INTEGER,
    difficulty_name VARCHAR(16)
) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM dict_tables.difficulties as difficulties
    WHERE difficulties.id = id_arg;
END;
$$ LANGUAGE plpgsql;
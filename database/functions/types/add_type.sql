DROP FUNCTION IF EXISTS add_type CASCADE;

CREATE OR REPLACE FUNCTION add_type(
    type_name_arg VARCHAR(16)
) 
RETURNS VOID AS $$
BEGIN
    INSERT INTO dict_tables.types(
        type_name
    ) VALUES (
        type_name_arg
    );
END;
$$ LANGUAGE plpgsql;
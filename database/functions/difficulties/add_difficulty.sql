DROP FUNCTION IF EXISTS add_difficulty CASCADE;

CREATE OR REPLACE FUNCTION add_difficulty(
    difficulty_name_arg VARCHAR(16)
) 
RETURNS VOID AS $$
BEGIN
    INSERT INTO dict_tables.difficulties(
        difficulty_name
    ) VALUES (
        difficulty_name_arg
    );
END;
$$ LANGUAGE plpgsql;
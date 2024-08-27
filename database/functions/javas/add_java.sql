DROP FUNCTION IF EXISTS add_java CASCADE;

CREATE OR REPLACE FUNCTION add_java(
    java_version_arg VARCHAR(32),
    java_url_arg VARCHAR(256)
) 
RETURNS VOID AS $$
BEGIN
    INSERT INTO dict_tables.javas(
        java_version,
        java_url
    ) VALUES (
        java_version_arg,
        java_url_arg
    );
END;
$$ LANGUAGE plpgsql;
DROP FUNCTION IF EXISTS check_is_hex CASCADE;

CREATE OR REPLACE FUNCTION check_is_hex(color TEXT) RETURNS BOOLEAN AS $$
BEGIN
    RETURN color ~* '^#[a-f0-9]{6}$';
END;
$$ LANGUAGE plpgsql;
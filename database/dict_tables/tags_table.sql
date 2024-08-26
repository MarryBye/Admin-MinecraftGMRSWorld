DROP TABLE IF EXISTS dict_tables.tags CASCADE;

$$ LANGUAGE plpgsql;
CREATE TABLE IF NOT EXISTS dict_tables.tags (
    id SERIAL PRIMARY KEY,
    tag_name VARCHAR(16),
    tag_color VARCHAR(7),

    CONSTRAINT check_is_hex CHECK (check_is_hex(tag_color))
)
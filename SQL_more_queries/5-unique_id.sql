-- Create table unique_id with id INT DEFAULT 1 and UNIQUE, name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

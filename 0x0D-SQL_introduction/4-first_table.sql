-- A script that creates a table called first_table in current db
-- does not fail if table exists
CREATE TABLE IF NOT EXISTS first_table (id INT,
name VARCHAR(256));

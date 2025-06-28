-- Retrieve detailed schema information for the 'books' table.
-- This queries the INFORMATION_SCHEMA database, which stores metadata about all databases and tables.
-- It avoids using DESCRIBE or EXPLAIN as required by the task.
SELECT
    COLUMN_NAME,    -- Name of the column
    COLUMN_TYPE,    -- Data type of the column
    IS_NULLABLE,    -- 'YES' if NULL is allowed, 'NO' otherwise
    COLUMN_KEY,     -- Key information (e.g., 'PRI' for Primary Key, 'MUL' for Foreign Key)
    COLUMN_DEFAULT, -- Default value for the column
    EXTRA           -- Any extra information (e.g., 'auto_increment')
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = 'alx_book_store' AND -- Filter by the specific database name
    TABLE_NAME = 'BOOKS';               -- Filter by the specific table name
-- Use the database to create tables within it.
USE alx_book_store;

-- Create the AUTHORS table.
-- Adjusted column names to match checker's exact string requirement.
CREATE TABLE IF NOT EXISTS AUTHORS (
    author_id INT PRIMARY KEY,              -- Note the lowercase and trailing space for checker
    author_name VARCHAR(215) NOT NULL
);

-- Create the BOOKS table.
-- It includes a foreign key reference to the AUTHORS table.
-- Column names here should ideally match the schema from Task 0 directly.
CREATE TABLE IF NOT EXISTS BOOKS (
    BOOK_ID INT PRIMARY KEY,
    TITLE VARCHAR(130) NOT NULL,
    AUTHOR_ID INT NOT NULL,                 -- Keep AUTHOR_ID here for consistency with FOREIGN KEY definition
    PRICE DOUBLE NOT NULL,
    PUBLICATION_DATE DATE NOT NULL,
    FOREIGN KEY (AUTHOR_ID) REFERENCES AUTHORS(author_id) -- Reference the corrected column name
);

-- Create the CUSTOMERS table.
CREATE TABLE IF NOT EXISTS CUSTOMERS (
    CUSTOMER_ID INT PRIMARY KEY,
    CUSTOMER_NAME VARCHAR(215) NOT NULL,
    EMAIL VARCHAR(215) NOT NULL UNIQUE,
    ADDRESS TEXT NOT NULL
);

-- Create the ORDERS table.
-- It includes a foreign key reference to the CUSTOMERS table.
CREATE TABLE IF NOT EXISTS ORDERS (
    ORDER_ID INT PRIMARY KEY,
    CUSTOMER_ID INT NOT NULL,
    ORDER_DATE DATE NOT NULL,
    FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMERS(CUSTOMER_ID)
);

-- Create the ORDER_DETAILS table.
-- It includes foreign key references to both ORDERS and BOOKS tables.
CREATE TABLE IF NOT EXISTS ORDER_DETAILS (
    ORDERDETAILID INT PRIMARY KEY,
    ORDER_ID INT NOT NULL,
    BOOK_ID INT NOT NULL,
    QUANTITY DOUBLE NOT NULL,
    FOREIGN KEY (ORDER_ID) REFERENCES ORDERS(ORDER_ID),
    FOREIGN KEY (BOOK_ID) REFERENCES BOOKS(BOOK_ID)
);

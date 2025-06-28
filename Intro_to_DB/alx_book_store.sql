-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS alx_book_store;

-- Use the newly created or existing database
USE alx_book_store;

-- Create the Authors table
CREATE TABLE IF NOT EXISTS Authors (
    author_id INT PRIMARY KEY,              -- Primary Key for Authors table
    author_name VARCHAR(215) NOT NULL       -- Name of the author
);

-- Create the Books table
CREATE TABLE IF NOT EXISTS Books (
    book_id INT PRIMARY KEY,                -- Primary Key for Books table
    title VARCHAR(130) NOT NULL,            -- Title of the book
    author_id INT NOT NULL,                 -- Foreign Key referencing Authors table
    price DOUBLE NOT NULL,                  -- Price of the book
    publication_date DATE NOT NULL,         -- Publication date of the book
    FOREIGN KEY (author_id) REFERENCES Authors(author_id) -- Define foreign key relationship
);

-- Create the Customers table
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT PRIMARY KEY,            -- Primary Key for Customers table
    customer_name VARCHAR(215) NOT NULL,    -- Name of the customer
    email VARCHAR(215) NOT NULL UNIQUE,     -- Email of the customer (must be unique)
    address TEXT NOT NULL                   -- Address of the customer
);

-- Create the Orders table
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT PRIMARY KEY,               -- Primary Key for Orders table
    customer_id INT NOT NULL,               -- Foreign Key referencing Customers table
    order_date DATE NOT NULL,               -- Date when the order was placed
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) -- Define foreign key relationship
);

-- Create the Order_Details table
CREATE TABLE IF NOT EXISTS Order_Details (
    orderdetailid INT PRIMARY KEY,          -- Primary Key for Order_Details table
    order_id INT NOT NULL,                  -- Foreign Key referencing Orders table
    book_id INT NOT NULL,                   -- Foreign Key referencing Books table
    quantity DOUBLE NOT NULL,               -- Quantity of the book in the order
    FOREIGN KEY (order_id) REFERENCES Orders(order_id), -- Define foreign key relationship
    FOREIGN KEY (book_id) REFERENCES Books(book_id)     -- Define foreign key relationship
);
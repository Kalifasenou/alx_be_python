-- Use the database to create tables within it.
USE alx_book_store;

-- Create the AUTHORS table.
CREATE TABLE IF NOT EXISTS AUTHORS (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);

-- Create the BOOKS table.
CREATE TABLE IF NOT EXISTS BOOKS (
    book_id INT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT NOT NULL,
    price DOUBLE NOT NULL,
    publication_date DATE NOT NULL,
    FOREIGN KEY (author_id) REFERENCES AUTHORS(author_id) 
);

-- Create the CUSTOMERS table.
CREATE TABLE IF NOT EXISTS CUSTOMERS (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL UNIQUE,
    address TEXT NOT NULL
);

-- Create the ORDERS table.
CREATE TABLE IF NOT EXISTS ORDERS (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES CUSTOMERS(customer_id)
);

-- Create the ORDER_DETAILS table.
CREATE TABLE IF NOT EXISTS ORDER_DETAILS (
    orderdetailid INT PRIMARY KEY,
    order_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity DOUBLE NOT NULL,
    FOREIGN KEY (order_id) REFERENCES ORDERS(order_id),
    FOREIGN KEY (book_id) REFERENCES BOOKS(book_id)
);

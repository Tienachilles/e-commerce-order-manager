CREATE DATABASE IF NOT EXISTS ecommerce;
USE ecommerce;

-- Disable foreign key checks temporarily
SET FOREIGN_KEY_CHECKS = 0;

-- Drop existing tables if they exist to start fresh
DROP TABLE IF EXISTS OrdersItems;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Customers;

-- Create Tables

CREATE TABLE Customers(
    CustomerID varchar(10) PRIMARY KEY,
    Name varchar(100) NOT NULL
);

CREATE TABLE Products(
    ProductID varchar(10) PRIMARY KEY,
    Name varchar(100) NOT NULL,
    Price decimal(10,2) NOT NULL
);

CREATE TABLE Orders (
    OrderID varchar(10) PRIMARY KEY,
    CustomerID varchar(10) NOT NULL,
    OrderDate date NOT NULL,
    Status varchar(50) DEFAULT 'Pending',
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE OrdersItems(
    OrderItemID INT AUTO_INCREMENT PRIMARY KEY,
    OrderID varchar(10) NOT NULL,
    ProductID varchar(10) NOT NULL,
    Quantity INT NOT NULL,
    Price decimal(10,2) NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Re-enable foreign key checks
SET FOREIGN_KEY_CHECKS = 1;

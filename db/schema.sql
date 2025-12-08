create  database if not exists  ecommerce;
use ecommerce;
-- create tables
-- tắt kiểm tra fk tạm thời
SET FOREIGN_KEY_CHECKS = 0;
-- drop các bảng mình định đặt tên
DROP TABLE IF EXISTS OrdersItems;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Customers;
-- bật lại khi kiểm tra xong
set FOREIGN_KEY_CHECKS = 0;
create table Customers(
	CustomerID varchar(10) primary key,
    Name varchar(100) not null
);


create table Products(
	ProductID varchar(10) primary key,
    Name varchar(100) not null,
    Price decimal(10,2) not null
);


create table Orders (
	OrderID varchar(10) primary key,
    CustomerID varchar(10) not null,
    OrderDate date not null,
    Status varchar(50) default 'Pending',
    foreign key(CustomerID) references Customers(CustomerID)
);


create table OrdersItems(
	OrderItemID INT AUTO_INCREMENT primary key,
    OrderID varchar(10) not null,
    ProductID varchar(10) not null,
    Quantity INT not null,
    Price decimal(10,2) not null,
    foreign key (OrderID) references Orders(OrderID),
    foreign key (ProductID) references Products(ProductID)
);
    
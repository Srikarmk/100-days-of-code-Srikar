create database employees;
use employees;
create table employees(	
	id INT auto_increment PRIMARY KEY,
    first_name varchar(100) NOT NULL,
    last_name varchar(100) NOT NULL, 
    middle_name varchar(100),
    age int not null,
    current_status varchar(100) not null DEFAULT "Employed"
    );
    desc employees;
    
    
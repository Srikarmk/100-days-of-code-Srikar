create database cats;
use cats;
CREATE TABLE cats (
    cat_id INT AUTO_INCREMENT,
    name VARCHAR(100),
    breed VARCHAR(100),
    age INT,
    PRIMARY KEY (cat_id)
); 
INSERT INTO cats(name, breed, age) 
VALUES ('Ringo', 'Tabby', 4),
       ('Cindy', 'Maine Coon', 10),
       ('Dumbledore', 'Maine Coon', 11),
       ('Egg', 'Persian', 4),
       ('Misty', 'Tabby', 13),
       ('George Michael', 'Ragdoll', 9),
       ('Jackson', 'Sphynx', 7);
DESC cats;
SELECT * FROM cats;
SELECT name,age FROM cats WHERE breed="tabby";
SELECT cat_id FROM cats;
SELECT name,breed FROM cats;
SELECT cat_id,age FROM cats WHERE cat_id=age;
SELECT name AS kitty_name FROM cats;
UPDATE cats SET age=5 WHERE cat_id=4;
UPDATE cats SET name="Jack" WHERE name="Jackson";
UPDATE cats SET breed="British ShortHair" WHERE name="Ringo";
UPDATE cats SET age=12 WHERE breed="maine coon";
SELECT * FROM cats WHERE name='Jackson'; 
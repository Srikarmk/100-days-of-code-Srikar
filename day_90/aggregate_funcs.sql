use books;

SELECT * FROM books;
SELECT DISTINCT author_lname from books;
SELECT COUNT(*) FROM books;
SELECT COUNT(DISTINCT author_fname) FROM books;
SELECT COUNT(*) FROM books WHERE title LIKE "%the%";

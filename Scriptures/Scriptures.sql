--Selects everything from the books table
SELECT *
FROM books;

--Queries the book name and number of chapters where the number of chapters is greater than or equal to 30
SELECT book_name,
    num_chapters
FROM books
WHERE num_chapters >= 30;

--Queries to show the book name and where it is located
SELECT section_name,
    book_name
FROM books
    INNER JOIN sections ON books.booksSections = sections.sections_id;

--Shows the number of books in each section
SELECT section_name AS "Section",
    COUNT(book_name) AS "Number of Books"
FROM books
    INNER JOIN sections ON books.booksSections = sections.sections_id
GROUP BY section_name;

--Shows the books with the most chapters and with the least chapters
SELECT SUM(num_chapters)  AS "Chapters in the scriptures"
FROM books;
SELECT  book_name,MAX(num_chapters) AS "Most Chapters"
FROM books;

SELECT book_name, MIN(num_chapters) AS "Least Chapters"
FROM books;


--Inserts a new book into the book of mormon prints to show it is added
INSERT INTO books
VALUES(null, 3, "Mahonri Moriancumer", 15);
SELECT *
FROM books
WHERE book_name == "Mahonri Moriancumer";

--Updates the new book to update the number of Chapters. prints to show it is updated
UPDATE books
set num_chapters = 52,
    book_name = "Mahonri"
WHERE book_name == "Mahonri Moriancumer";
SELECT *
FROM books
WHERE book_name == "Mahonri";

--Deletes the new book Mahonri prints to show it is deleted
DELETE FROM books
WHERE book_name == "Mahonri";
SELECT *
FROM books
WHERE booksSections == 3;
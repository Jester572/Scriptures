# Overview


This software is a two part software. The first is a python file using sqlite3 to create and populate a database. There is no database in this file so the python file must be run first. The second file is a .sql file, this has queries that demonstrate my knowledge in learning about SQL.

This database contains the sections of the scriptures and each book within those sections. It also contains the number of chapters within each book. This is to help in knowing which books have the most chapters and comparing them all.


[Software Demo Video](https://youtu.be/DJrvk6VN49Y)

# Relational Database

The database I am using is one created by running the python file called scriptures.db

There are two tables that are created, the sections table, and the books table. The section table consists of the five different sections of the scriptures (Old Testament, New Testament, Book of Mormon, Doctrine & Covenants, Pearl of Great Price). The books table is a child of the sections table by using a foreign key. Each book has an auto generated ID number and the number of chapters of each book.

# Development Environment

Visual Studio Code

Languages:Python, SQL

Libraries:sqlite3, SQlite

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [W3 Schools](https://www.w3schools.com/sql/)
- [Youtube-sentdex](https://www.youtube.com/watch?v=NCc5r7Wr7gg)

# Future Work


- Learn to combine a max and min into one query
- Create subqueries to get better information and usage
- Better understand all the different joins and implement them into my code.

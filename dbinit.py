import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#createTable = "CREATE TABLE IF NOT EXISTS books (BookID INTEGER PRIMARY KEY,BookName TEXT,AuthorID TEXT ,price INTEGER,Journal TEXT )"
createTable = "CREATE TABLE IF NOT EXISTS authors (AuthorID INTEGER PRIMARY KEY,AuthorName TEXT,Country TEXT)"
# alter_table_sql = '''
# ALTER TABLE books
# ADD FOREIGN KEY (AuthorID) REFERENCES authors(AuthorID);
# '''
create_books_table_sql = '''
CREATE TABLE IF NOT EXISTS books (
    BookID INTEGER PRIMARY KEY,
    BookName TEXT,
    AuthorID INTEGER,
    price INTEGER,
    Journal TEXT,
    FOREIGN KEY (AuthorID) REFERENCES authors(AuthorID)
);
'''
create_users_table_sql = '''
CREATE TABLE IF NOT EXISTS users (
UserID INTEGER PRIMARY KEY,
UserName TEXT,
Email TEXT,
MobileNumber TEXT
)
'''
create_transaction_table_sql = '''
CREATE TABLE IF NOT EXISTS transactions (
BookID INTEGER,
UserID INTEGER,
Date DATE,
isReturned BOOLEAN,
FOREIGN KEY (BookID) REFERENCES books(BookID),
FOREIGN KEY (UserID) REFERENCES users(UserID)

)
'''
cursor.execute(create_transaction_table_sql)
connection.commit()
# Sample data to be inserted into the books table
sample_user_data = [
    (1, 'Kishore', "kishorekumararcot@gmail.com","9043318453"),
    (2, 'Dinesh', "dk1802@gmail.com", '9833823253'),
    (3, 'Sathish',"sathish@gmail", '993293738'),
    (4, 'virat kohli', "virat&gmail.com" , '923823823')
]
sample_books_data = [
    (1, 'The Great Gatsby', 101, 20, 'Novel'),
    (2, 'To Kill a Mockingbird', 102, 25, 'Novel'),
    (3, '1984', 103, 15, 'Dystopian Fiction'),
    (4, 'Pride and Prejudice', 104, 18, 'Classic Literature')
]
sample_author_data = [
    (101, 'F. Scott Fitzgerald', 'United States'),
    (102, 'Harper Lee', 'United States'),
    (103, 'George Orwell', 'United Kingdom'),
    (104, 'Jane Austen', 'United Kingdom'),
    (105, 'Agatha Christie', 'United Kingdom'),
    (106, 'Leo Tolstoy', 'Russia'),
    (107, 'J.K. Rowling', 'United Kingdom'),
    (108, 'Gabriel García Márquez', 'Colombia')
]
sample_transaction_data = [
    (1, 1, '2023-10-03', 1),  # BookID, UserID, Date (in 'YYYY-MM-DD' format), isReturned (1 for True, 0 for False)
    (2, 2, '2023-09-25', 0),
    (3, 3, '2023-09-28', 1),
    (4, 4, '2023-10-01', 0),
    (1, 5, '2023-09-27', 1),
    (2, 6, '2023-10-02', 0)

]

# Insert the sample data into the books table
insert_books_sql = "INSERT INTO books (BookID, BookName, AuthorID, price, Journal) VALUES (?, ?, ?, ?, ?)"
insert_users_sql = "INSERT INTO users (UserID,UserName,Email,MobileNumber) VALUES (?,?,?,?)"
insert_authors_sql = "INSERT INTO authors (AuthorID, AuthorName,Country) VALUES (?,?,?)"
insert_transaction_sql = "INSERT INTO transactions (BookID,UserID,Date,isReturned) VALUES (?,?,?,?)"
for data in sample_transaction_data:
    cursor.execute(insert_transaction_sql, data)
    connection.commit()

# cursor.execute(INSERT INTO users (UserID,UserName,Email,MobileNumber) VALUES (?,?,?,?),)
#cursor.execute("SELECT books.BookName,authors.AuthorID FROM books INNER JOIN authors ON books.AuthorID=authors.AuthorID")                                                           
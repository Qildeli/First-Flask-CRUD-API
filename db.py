import sqlite3

conn = sqlite3.connect('books.db')

c = conn.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS book (
    id INTEGER PRIMARY KEY,
    author TEXT NOT NULL,
    language TEXT NOT NULL,
    title TEXT NOT NULL
    )""")

# conn.commit()

c.execute("INSERT INTO book (id, author, language, title) VALUES (1, 'Rowling', 'English', 'Harry Potter' )")

conn.commit()

conn.close()

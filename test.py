import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_query = "CREATE TABLE users (id int, username text, password text)"

cursor.execute(create_query)

insert_query = 'INSERT INTO users VALUES (?, ?, ?)'

users = [
    (1, 'ayan', 'abcd'),
    (2, 'ram', 'efgh'),
    (3, 'sita', 'ijkl'),
    (4, 'hanuman', 'mnop')
]

cursor.executemany(insert_query, users)

select_query = 'SELECT * FROM users'
[print(user) for user in cursor.execute(select_query)]

connection.commit()
connection.close()
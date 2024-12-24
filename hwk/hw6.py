import sqlite3
connection = sqlite3.connect('../hws/users.db')
cursor = connection.cursor()

users_db =("""
    CREATE TABLE IF NOT EXISTS users (
    fio VARCHAR(100) NOT NULL,
    AGE INTEGER NOT NULL,
    HOBBY TEXT
    )
""")
cursor.execute(users_db)
connection.commit()

def add_user(fio, age, hobby=()):
    cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (fio, age, hobby))
    connection.commit()
    print(f'user:{fio}, added')
add_user('monkey_d_luffy', 19, 'became king of pirates' )

def get_user_by_age(age):
    cursor.execute('SELECT *  FROM users  WHERE age = ?', (age,))

    users = cursor.fetchall()
    print(users)
get_user_by_age(19)


connection.close()
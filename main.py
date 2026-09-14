import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("""CREATE TABEL IF NOT EXISTS USERS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME VARCHAR(50) NOT NULL,
            SURNAME VARCHAR(50) NOT NULL,
            EMAIL VARCHAR(50) NOT NULL UNIQUE,
            PHONE VARCHAR(50) NOT NULL,""")
cur.execute("""CREATE TABEL IF NOT EXISTS transactions(
               ID INTEGER PRIMARY KEY AUTOINCREMENT,
               amount decimal(10,2) NOT NULL,
               user_from_id INTEGER NOT NULL,
               user_to_id INTEGER NOT NULL,
               data VARCHAR NOT NULL,
               FORGEIN KEY (user_from_id) REFERENCES USERS(ID),
               FORGEIN KEY (user_to_id) REFERENCES transactions(ID),
               """)
import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("""CREATE TABEL IF NOT EXISTS USERS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME VARCHAR(50) NOT NULL,
            SURNAME VARCHAR(50) NOT NULL,
            EMAIL VARCHAR(50) NOT NULL UNIQUE,
            PHONE VARCHAR(50) NOT NULL,""")

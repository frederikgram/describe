import sqlite3

conn = sqlite3.connect('images.db')
cur = conn.cursor()
cur.execute('CREATE TABLE images (id integer PRIMARY KEY, path text UNIQUE NOT NULL, metadata text);')
conn.commit()

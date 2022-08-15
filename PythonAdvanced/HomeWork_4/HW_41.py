import sqlite3

db = sqlite3.connect('test.sqlite3')
c = db.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS bank (
id INTEGER AUTO_INCREMENT PRIMARY KEY,
Назначение TEXT,
Сума REAL,
Время DATE

)''')
db.commit()
db.close()

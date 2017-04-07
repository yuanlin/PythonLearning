import sqlite3

conn = sqlite3.connect('DB.sqlite')
cur = conn.cursor()

sqlStr = 'insert into homework2 (id, data) values (1, "Unit09作業二")'
cur.execute(sqlStr)

conn.commit()
conn.close()
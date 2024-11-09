import sqlite3

connection = sqlite3.connect("itstep_DB.s13",)

cur = connection.cursor()

#cur = connection.cursor()
#cur.execute("CREATE TABLE first_table (name TEXT);")

#cur = connection.cursor()
#cur.execute("CREATE TABLE Test_table (Id INT,Name TEXT);")

#cur = connection.cursor()
#cur.execute("INSERT INTO first_table (name) VALUES ('NIKE');")

#cur = connection.cursor()
cur.execute("SELECT rowid, name FROM first_table;")
res=cur.fetchall()

print(res)

for item in res:
    print("Row id:",item[0],"\tName:",item[1])

connection.commit()
connection.close()
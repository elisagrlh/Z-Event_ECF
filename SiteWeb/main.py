import sqlite3

connection = sqlite3.connect("login.db")
cursor = connection.cursor()

cursor.execute("create table login (email text, password text)")

login_list = [
    ("streamer@example.com", "streamer123"),
    ("bigstreamer@example.com", "bigstreamer123")
]

cursor.executemany("insert into login values (?,?)", login_list)


#print databse rows
for row in cursor.execute("select * from login"):
    print(row)

#print specific rows
print("****************************************")
cursor.execute("select * from login where email=:s", {"s": "bigstreamer@example.com"})
login_search = cursor.fetchall()   
print(login_search)

connection.close()
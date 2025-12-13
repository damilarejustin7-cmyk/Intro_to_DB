import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",              # or 'damilarejustin'
    password="Damilare2004$",
    database="alx_book_store"
)

cursor = mydb.cursor()
cursor.execute("SELECT DATABASE();")
print(cursor.fetchone())

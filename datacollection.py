import psycopg2

conn = psycopg2.connect(database="oltpdb",
                        host="localhost",
                        user="postgres",
                        password="admin@123",
                        port="5432")

cursor = conn.cursor()
cursor.execute("SELECT * FROM cobrand")
print(cursor.fetchone())
print(cursor.fetchall())

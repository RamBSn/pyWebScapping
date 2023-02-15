import sqlite3

select_query1 = "SELECT band, date FROM events WHERE date='2025.12.25'"
select_query2 = "SELECT * FROM events"

# create a connection and cursor
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# select statements
cursor.execute(select_query1)
row1 = cursor.fetchall()
print(row1)
cursor.execute(select_query2)
rows = cursor.fetchall()
print(rows)

# #  insert data
# new_data = [('band4','city4','date4'), ('band5','city5','date5')]
# cursor.executemany("INSERT INTO events VALUES (?,?,?)", new_data)
# connection.commit()

# # delete data
# cursor.execute("DELETE FROM events where band='band5'")
# connection.commit()
import sqlite3

con = sqlite3.connect('database.db')
my_cursor = con.cursor()

def add(title, description):
    my_cursor.execute(f"INSERT INTO tasks (title, description) VALUES ('{title}', '{description}')")
    con.commit()
    
def getAll():
    my_cursor.execute("SELECT * FROM tasks")
    results = my_cursor.fetchall()
    return results
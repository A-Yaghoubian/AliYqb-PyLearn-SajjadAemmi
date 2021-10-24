import sqlite3

con = sqlite3.connect('database.db')
my_cursor = con.cursor()

def add(title, done, description, priority, date, time):
    my_cursor.execute(f"INSERT INTO tasks (title, done, description, priority, date, time) VALUES ('{title}', '{done}', '{description}', '{priority}', '{date}', '{time}')")
    con.commit()
    
def getAll():
    my_cursor.execute("SELECT * FROM tasks")
    results = my_cursor.fetchall()
    return results

def remove(title):
    my_cursor.execute(f"DELETE FROM tasks WHERE title = '{title}'")
    con.commit()
    
def updateDo(title):
    my_cursor.execute(f"UPDATE tasks SET done = '1' WHERE title = '{title}'")
    con.commit()
    
def updateUndo(title):
    my_cursor.execute(f"UPDATE tasks SET done = '0' WHERE title = '{title}'")
    con.commit()
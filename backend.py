import sqlite3

def connect():
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS machine (id INTEGER PRIMARY KEY, date TEXT, tech TEXT)")
    conn.commit()
    conn.close()

def insert(date,tech):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO machine VALUES (NULL,?,?)", (date, tech))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM machine")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(date="", tech=""):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM machine WHERE date=? OR tech=?",(date, tech))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM machine WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,date,tech):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE machine SET date=?, tech=? WHERE id=?", (id,date,tech))
    conn.commit()
    conn.close()

connect()
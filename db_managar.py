import sqlite3

def create_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute('''
            CREATE TABLE IF NOT EXISTS items
            ([timestamp] joiningDate, [intern] TEXT, [specialist] TEXT)
            ''')
                                    
    conn.commit()

def add_item(timestamp, intern, specialist):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    sql = ''' INSERT INTO items(timestamp, intern, specialist)
              VALUES(?,?,?) '''

    c.execute(sql,(timestamp, intern, specialist))
    conn.commit()

def is_exist(timestamp, intern, specialist):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute('''SELECT *
            FROM items
            WHERE timestamp=? and intern=? and specialist=?
            ''', (timestamp, intern, specialist))

    result = c.fetchall()

    return any(result)

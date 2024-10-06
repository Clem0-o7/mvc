import sqlite3

DATABASE = 'traffic_lights.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def init_db():
    with connect_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS traffic_lights (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                location TEXT NOT NULL,
                status TEXT NOT NULL
            )
        ''')

def get_all_traffic_lights():
    with connect_db() as conn:
        return conn.execute('SELECT * FROM traffic_lights').fetchall()

def get_traffic_light(id):
    with connect_db() as conn:
        return conn.execute('SELECT * FROM traffic_lights WHERE id = ?', (id,)).fetchone()

def add_traffic_light(location, status):
    with connect_db() as conn:
        conn.execute('INSERT INTO traffic_lights (location, status) VALUES (?, ?)', (location, status))

def update_traffic_light(id, location, status):
    with connect_db() as conn:
        conn.execute('UPDATE traffic_lights SET location = ?, status = ? WHERE id = ?', (location, status, id))

def delete_traffic_light(id):
    with connect_db() as conn:
        conn.execute('DELETE FROM traffic_lights WHERE id = ?', (id,))

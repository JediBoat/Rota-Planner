import sqlite3
from tkinter.font import names

class Database:
    def __init__(self, db_name = "rota_planner.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
    
    def create_tables(self):
        # Create an employees table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                dep TEXT NOT NULL
            )
        """)
        # Create an events table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                details TEXT NOT NULL
            )
        """)
        #times table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS times (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_times TEXT NOT NUll
            )
        """)
        self.connection.commit()

    def add_employee(self, name):#need to stop duplicates
        self.cursor.execute("""
            INSERT INTO employees (name)
            VALUES (?)
        """, (name,))
        self.connection.commit()

    def search_employees(self):
        self.cursor.execute("SELECT name FROM employees")
        return [row[0] for row in self.cursor.fetchall()]

    def search_events(self):
        self.cursor.execute("SELECT * FROM events")
        return self.cursor.fetchall()

    def remove_employee(self, names):
        self.cursor.executemany(
            """
            DELETE FROM employees
            WHERE name = ?
            """,
            [(name,) for name in names]
        )
        self.connection.commit()

    def get_events(self):
        self.cursor.execute("SELECT name, details FROM events")
        return self.cursor.fetchall()
    
    def add_event(self, name, details):
        self.cursor.execute("""
            INSERT INTO events (name, details)
            VALUES (?, ?)
        """, (name, details))
        self.connection.commit()

    def remove_event(self, name):
        self.cursor.execute("""
            DELETE FROM events
            WHERE name = ?
        """, (name,))
        self.connection.commit()

    def get_event_names(self):
        self.cursor.execute("SELECT name FROM events")
        return [row[0] for row in self.cursor.fetchall()]
    
    def update_event(self, name, new_details):
        self.cursor.execute("""
            UPDATE events
            SET details = ?, 
            name = ?
            WHERE name = ?
        """, (new_details, name))
        self.connection.commit()
    

    def close_connection(self):
        self.connection.close()

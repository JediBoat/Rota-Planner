import sqlite3

class Database:
    def __init__(self, db_name = "rota_planner.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        # Create an employees table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
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
        self.connection.commit()

    def add_employee(self, name):
        self.cursor.execute("""
            INSERT INTO employees (name)
            VALUES (?)
        """, (name,))
        self.connection.commit()

    def search_employees(self):
        self.cursor.execute("SELECT * FROM employees")
        return self.cursor.fetchall()

    def search_events(self):
        self.cursor.execute("SELECT * FROM events")
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()

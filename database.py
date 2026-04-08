import sqlite3

DB_PATH = "/tmp/multi_agent.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Ensure tables exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        note TEXT
    )
    """)

    conn.commit()
    return conn


def add_task(task):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
        conn.close()
        return "Task saved successfully"
    except Exception as e:
        return f"Task error: {str(e)}"


def save_note(note):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (note) VALUES (?)", (note,))
        conn.commit()
        conn.close()
        return "Note saved successfully"
    except Exception as e:
        return f"Note error: {str(e)}"
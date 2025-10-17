import sqlite3
import os
DB_NAME = "../allatmenhely.db"
MIGRATIONS_DIR = "./migrations"

def get_applied_migrations(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS migrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT UNIQUE,
            applied_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    result = conn.execute("SELECT filename FROM migrations").fetchall()
    return {row[0] for row in result}

def apply_migration(conn, filename):
    path = os.path.join(MIGRATIONS_DIR, os.listdir(MIGRATIONS_DIR)[0])

    with open(path, "r", encoding="utf-8") as file:
        sql = file.read()

    conn.executescript(sql)
    conn.execute("INSERT INTO migrations (filename) VALUES (?)", (filename,))
    conn.commit()

    print(f"Lefuttatva: {filename}")


def migrate():
    conn = sqlite3.connect(DB_NAME)
    applied = get_applied_migrations(conn)

    migrations = sorted(f for f in os.listdir(MIGRATIONS_DIR) if f.endswith(".sql"))

    for m in migrations:
        if m not in applied:
            apply_migration(conn, m)
        else:
            print(f"Kihagyva (már lefuttatva): {m}")

if __name__ == "__main__":
    migrate()
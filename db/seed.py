import os
import sqlite3

DB_NAME = "../allatmenhely.db"
SEEDS_DIR = "./seeds"

def get_applied_seeds(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS seeds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT UNIQUE,
            applied_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    result = conn.execute("SELECT filename FROM seeds").fetchall()
    return {row[0] for row in result}

def run_seed(conn, filename):
    path = os.path.join(SEEDS_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        sql = f.read()
    print(f"Futtatás: {filename}")

    conn.execute(sql)
    conn.execute("INSERT INTO seeds (filename) VALUES (?)", (filename,))
    conn.commit()

def seed():
    if not os.path.exists(SEEDS_DIR):
        print("Nincs seeds mappa!")
        return

    with sqlite3.connect(DB_NAME) as conn:
        applied_seeds = get_applied_seeds(conn)
        seeds = sorted(f for f in os.listdir(SEEDS_DIR) if f.endswith(".sql"))
        print(f"Seeds: {applied_seeds}")
        for s in seeds:
            if s not in applied_seeds:
                run_seed(conn, s)
            else:
                print(f"Kihagyva (már lefuttatva): {s}")

if __name__ == "__main__":
    seed()
    print("Seedelés kész!")
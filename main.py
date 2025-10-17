import sqlite3
try:
    conn = sqlite3.connect('allatmenhely.db')
    cursor = conn.cursor()
    print("Sikeres kapcsolódat az adatbázishoz!")

    cursor.execute("DROP TABLE IF EXISTS telephelyek")

    query = """
            CREATE TABLE telephelyek (
                ID INT PRIMARY KEY NOT NULL
            )"""

    cursor.execute(query)
    conn.commit()

except sqlite3.Error as error:
    print("Error: ",error)

finally:
    if conn:
        conn.close()
        print("Az adatbázis kapcsolat bezárva.")

if __name__ == '__main__':
    print(conn)
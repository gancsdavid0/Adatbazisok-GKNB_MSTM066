import sqlite3
from menu import Menu
DB_NAME = "./allatmenhely.db"

def main():
    with sqlite3.connect(DB_NAME) as conn:
        if conn:
            app_menu = Menu(conn)
            app_menu.Menu()

if __name__ == '__main__':
    main()
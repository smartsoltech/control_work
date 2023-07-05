import sqlite3
from os import getenv
from pathlib import Path

DB_TYPE = getenv("DB_TYPE")
DB_PATH = Path(getenv("DB_PATH"))
DB_NAME = getenv("DB_NAME")
DB_FILE = DB_PATH / DB_NAME

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(str(DB_FILE))
        return conn
    except sqlite3.Error as error:
        print("Error while connecting to SQLite", error)

def setup_database():
    conn = create_connection()
    if conn is not None:
        # Создание таблицы domestic_animals
        create_table(conn, """CREATE TABLE IF NOT EXISTS domestic_animals (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                command TEXT,
                                birth_date TEXT
                            )""")
        
        # Создание таблицы farm_animals
        create_table(conn, """CREATE TABLE IF NOT EXISTS farm_animals (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                command TEXT,
                                birth_date TEXT
                            )""")
        
        # Создание таблицы young_animals
        create_table(conn, """CREATE TABLE IF NOT EXISTS young_animals (
                                id INTEGER PRIMARY KEY,
                                animal_id INTEGER,
                                age_months INTEGER,
                                FOREIGN KEY (animal_id) REFERENCES domestic_animals(id) 
                                    ON DELETE CASCADE 
                                    ON UPDATE CASCADE
                            )""")
        
        # Создание таблицы all_animals
        create_table(conn, """CREATE TABLE IF NOT EXISTS all_animals (
                                id INTEGER PRIMARY KEY,
                                animal_id INTEGER,
                                animal_type TEXT,
                                previous_table TEXT,
                                FOREIGN KEY (animal_id) REFERENCES domestic_animals(id) 
                                    ON DELETE CASCADE 
                                    ON UPDATE CASCADE
                            )""")
    else:
        print("Error: Failed to create database connection.")

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("Table created successfully")
    except sqlite3.Error as e:
        print(e)

def insert_record(table, data):
    conn = create_connection()
    print(f'Вызов функции insert_record с агрументами: {table}, {data}')
    if conn is not None:
        try:
            c = conn.cursor()
            if table == 1:
                print(f'Запись данных {data} в таблицу {table}')
                c.execute("INSERT INTO domestic_animals (name, command, birth_date) VALUES (?, ?, ?)", data)
            elif table == 2:
                print(f'Запись данных {data} в таблицу {table}')
                c.execute("INSERT INTO farm_animals (name, command, birth_date) VALUES (?, ?, ?)", data)
            conn.commit()
            print("Record inserted successfully")
        except sqlite3.Error as e:
            print(e)
    else:
        print("Error: Failed to create database connection.")

def delete_record(table, id):
    conn = create_connection()
    if conn is not None:
        try:
            c = conn.cursor()
            if table == 1:
                c.execute("DELETE FROM domestic_animals WHERE id=?", (id,))
            elif table == 2:
                c.execute("DELETE FROM farm_animals WHERE id=?", (id,))
            conn.commit()
            print("Record deleted successfully")
        except sqlite3.Error as e:
            print(e)
    else:
        print("Error: Failed to create database connection.")

def view_records(table):
    conn = create_connection()
    if conn is not None:
        try:
            c = conn.cursor()
            if table == 1:
                c.execute("SELECT * FROM domestic_animals")
                rows = c.fetchall()
                for row in rows:
                    print(row)
            elif table == 2:
                c.execute("SELECT * FROM farm_animals")
                rows = c.fetchall()
                for row in rows:
                    print(row)
        except sqlite3.Error as e:
            print(e)
    else:
        print("Error: Failed to create database connection.")

def search_records(table, keyword):
    conn = create_connection()
    if conn is not None:
        try:
            c = conn.cursor()
            if table == 1:
                c.execute("SELECT * FROM domestic_animals WHERE name LIKE ? OR command LIKE ?", ('%' + keyword + '%', '%' + keyword + '%'))
                rows = c.fetchall()
                for row in rows:
                    print(row)
            elif table == 2:
                c.execute("SELECT * FROM farm_animals WHERE name LIKE ? OR command LIKE ?", ('%' + keyword + '%', '%' + keyword + '%'))
                rows = c.fetchall()
                for row in rows:
                    print(row)
        except sqlite3.Error as e:
            print(e)
    else:
        print("Error: Failed to create database connection.")

def export_records(table, filename):
    conn = create_connection()
    if conn is not None:
        try:
            c = conn.cursor()
            if table == 1:
                c.execute("SELECT * FROM domestic_animals")
                rows = c.fetchall()
                with open(filename, 'w') as f:
                    for row in rows:
                        f.write(','.join(map(str, row)) + '\n')
                print(f"Records exported to {filename} successfully")
            elif table == 2:
                c.execute("SELECT * FROM farm_animals")
                rows = c.fetchall()
                with open(filename, 'w') as f:
                    for row in rows:
                        f.write(','.join(map(str, row)) + '\n')
                print(f"Records exported to {filename} successfully")
        except sqlite3.Error as e:
            print(e)
    else:
        print("Error: Failed to create database connection.")

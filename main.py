import __init__
from os import getenv
from pathlib import Path
import sqlite3
from db import create_connection, setup_database, insert_record, delete_record, view_records, search_records


print(f'Database type: {getenv("DB_TYPE")}')
# print(f'Database file path: {db_path / db_name}')
# print('Environment loaded successful')

def show_main_menu():
    print("Выберите действие:")
    print("1. Добавить запись")
    print("2. Удалить запись")
    print("3. Просмотреть записи")
    print("4. Поиск")
    print("5. Выход")

    return int(input("Ваш выбор: "))

def show_tables_menu():
    print("Выберите таблицу:")
    print("1. Домашние животные")
    print("2. Животные фермы")
    # Добавьте здесь другие таблицы по мере необходимости

    return int(input("Ваш выбор: "))


def main_test():
    print('Main.py started')
    db_type = getenv("DB_TYPE")
    db_path = Path(getenv("DB_PATH"))
    db_name = getenv("DB_NAME")
    print(f'Database type: {db_type}')
    print(f'Database file path: {db_path / db_name}')
    print('Environment loaded successful')

    if db_type == 'sqlite':
        try:
            # создаем подключение к базе данных SQLite
            conn = create_connection()
            # создаем базу данных
            try:
                setup_database()
                print("Database setup completed successfully")
            except Exception as e:
                print("Failed to setup the database", e)
        except sqlite3.Error as error:
            print("Failed to connect to SQLite", error)
        finally:
            if conn:
                conn.close()
                print("SQLite connection is closed")
    else:
        print("Unsupported database type")

    while True:
        action = show_main_menu()
        if action == 1:
            table = show_tables_menu()
            data = input("Введите Класс, Имя, команды и дата рождения, через пробел: ")
            insert_record(table, data)
        elif action == 2:
            table = show_tables_menu()
            id = int(input("Введите номер записи для удаления: "))
            delete_record(table, id)
        elif action == 3:
            table = show_tables_menu()
            view_records(table)
        elif action == 4:
            table = show_tables_menu()
            term = input("Введите строку поиска: ")
            search_records(table, term)
        elif action == 5:
            print("Выход...")
            break


main_test()


import __init__
from os import getenv
from pathlib import Path
import sqlite3
import db
from test import validate_data_input, validate_table_choice, validate_menu_choice

class Counter():
    def __init__(self):
        self.value = 0

    def add(self):
        self.value += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            # Нет исключений, ресурс был успешно использован
            return True
        else:
            # Было возбуждено исключение, ресурс не был корректно использован
            return False

class Animal:
    def __init__(self, type, name, commands, birthdate):
        self.type = type
        self.name = name
        self.commands = commands
        self.birthdate = birthdate

    def to_dict(self):
        return [self.name, self.commands, self.birthdate]

        
def add_record(table):
    while True:
        with Counter() as count:
            print("Введите данные для новой записи, разделенные пробелом:")
            data = input().split()
        
            try:
                validate_data_input(data)
                validate_table_choice(table)

                if len(data) < 4:
                    raise ValueError("Недостаточно данных для создания записи.")
                
                if table == 1:
                    with Counter() as counter:
                        counter.add()
                        animal = Animal(type=data[0], name=data[1], commands=data[2], birthdate=data[3])
                        animal_data = (animal.name, animal.commands, animal.birthdate)
                        db.insert_record(table=table, data=animal_data)
                        print("Запись успешно добавлена")
                else:
                    print("Выбрана некорректная таблица")
                    
                break  # Break out of the loop if input is valid

            except ValueError as e:
                print("Ошибка: ", e)


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
    return int(input("Ваш выбор: "))


def main_test():
    print('Main.py started')
    db_type = getenv("DB_TYPE")
    db_path = Path(getenv("DB_PATH"))
    db_name = getenv("DB_NAME")
    print(f'Database type: {db_type}')
    print(f'Database file path: {db_path / db_name}')
    print('Environment loaded successful')
    try:
        # создаем подключение к базе данных SQLite
        conn=db.create_connection()
        # создаем базу данных
        try:
            db.setup_database()
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
            choice = show_main_menu()
            try:
                validate_menu_choice(choice)

                if choice == 1:
                    while True:
                        table_choice = show_tables_menu()
                        try:
                            validate_table_choice(table_choice)

                            if table_choice == 1:
                                add_record(1)
                            elif table_choice == 2:
                                add_record(2)
                            break

                        except ValueError as e:
                            print("Ошибка: ", e)

                elif choice == 2:
                    table = show_tables_menu()
                    id = int(input("Введите номер записи для удаления: "))
                    db.delete_record(table, id)
                    print(f'Передача параметров в функцию {table}, {id}')     
                elif choice == 3:
                    table = show_tables_menu()
                    db.view_records(table)
                elif choice == 4:
                    table = show_tables_menu()
                    term = input("Введите строку поиска: ")
                    db.search_records(table, term)
                elif choice == 5:
                    print("Выход...")
                    break

            except ValueError as e:
                print("Ошибка: ", e)

    except sqlite3.Error as error:
        print("Failed to connect to SQLite", error)
        
main_test()


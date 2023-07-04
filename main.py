import __init__
from os import getenv
from pathlib import Path
import sqlite3
import db


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
    with Counter() as count:
        print("Введите данные для новой записи, разделенные пробелом:")
        data = input().split()
        info = Animal(type=data[0], name=data[1], commands=data[2], birthdate=data[3])
        # print(info.name)
        # print(info.type)
        # print(info.commands)
        # print(info.birthdate)
        if len(data) == 4:
                count.add()
                # Создаем объект класса Animal и передаем значения в конструктор
                animal = Animal(type=data[0], name=data[1], commands=data[2], birthdate=data[3])
                # Извлекаем значения из объекта Animal
                animal_data = (animal.name, animal.commands, animal.birthdate)
                # Вставляем данные в таблицу
                db.insert_record(table, animal_data)
                print("Запись успешно добавлена")
        else:
            raise ValueError("Неверный формат данных. Заполните все поля.")
# print(f'Database type: {getenv("DB_TYPE")}')
# # print(f'Database file path: {db_path / db_name}')
# # print('Environment loaded successful')

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

    if db_type == 'sqlite':
        try:
            # создаем подключение к базе данных SQLite
            conn = db.create_connection()
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
        action = show_main_menu()
        if action == 1:
            add_record(1)
        elif action == 2:
            table = show_tables_menu()
            id = int(input("Введите номер записи для удаления: "))
            db.delete_record(table, id)
            print(f'Передача параметров в функцию {table}, {id}')
        elif action == 3:
            table = show_tables_menu()
            db.view_records(table)
            print(f'Передача параметров в функцию {table}')
        elif action == 4:
            table = show_tables_menu()
            term = input("Введите строку поиска: ")
            db.search_records(table, term)
            print(f'Передача параметров в функцию {table}, {term}')
        elif action == 5:
            print("Выход...")
            break


main_test()


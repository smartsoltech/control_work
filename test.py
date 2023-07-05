def validate_data_input(data):
    if len(data) != 4:
        raise ValueError("Неверный формат данных. Заполните все поля.")

def validate_table_choice(table):
    if table not in [1, 2]:
        raise ValueError("Выбрана некорректная таблица.")

def validate_menu_choice(choice):
    if choice not in [1, 2, 3, 4, 5]:
        raise ValueError("Выбрано некорректное действие.")
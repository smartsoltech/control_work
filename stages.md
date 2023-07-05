# Выполнение заданий 1-5
# windows host
1. создание папки на компе, загрузка а Visual studio
* python -m venv .venv
* touch .gitignore
* touch .env
* git init
* git add .
* git commit -m "init commit"
* git remote add orogin https://github.com/smartsoltech/control_work.git
* git push origin master

# llinux host
* sudo -i
* cd /opt
* git clone https://github.com/smartsoltech/control_work.git
* cd control_work
* cd tasks1-5
* cat > domestic_animals.txt
* > ```Собака```
* > ```Кошка```
* > ```Хомяк```
* Нажал CTRL+D
* cat > farm_animals.txt
* > ```Лошадь```
* > ```Верблюд```
* > ```Осёл```
* Нажал CTRL+D

Для проверки содержимого файлов:

* > cat domestic_animals.txt
 > ```Собака```

 > ```Кошка```

 > ```Хомяк```
м
* > cat domestic_animals.txt 
 > ```Лошадь```

 > ```Верблюд```

 > ```Осёл```


 * Объединение файлов в один командой cat
 > ```cat domestic_animals.txt farm_animals.txt > human_friends.txt```
 
 проверка содержимого:
 * > cat human_friends.txt

  > ```Собака```

 > ```Кошка```

 > ```Хомяк```

 > ```Лошадь```

 >```Верблюд```

 > ``` Осёл```

# Создание директориии и перемещение файла в нее
> ``` mkdir tmp_folder```

> ```mv human_friends.txt ./tmp_folder/human_friends.txt```


# Создание БД MySQL

> ``` > mysql -u root -p ```

> ```CREATE DATABASE FriendsOfMan;```

> ```USE FriendsOfMan;```

# Cоздание таблиц:

> CREATE TABLE domestic_animals (
>    ID INT PRIMARY KEY AUTO_INCREMENT,
>    Species VARCHAR(100),
>    Name VARCHAR(100),
>    Command VARCHAR(100),
>    BirthDate DATE
> );

> CREATE TABLE farm_animals (
>    ID INT PRIMARY KEY AUTO_INCREMENT,
>    Species VARCHAR(100),
>    Name VARCHAR(100),
>    Command VARCHAR(100),
>    BirthDate DATE
> );

# Добавление данных в таблицу domestic_animals

> INSERT INTO domestic_animals (Species, Name, Command, BirthDate) VALUES ('Dog', 'Rex', 'Sit', '2021-01-01');

> INSERT INTO domestic_animals (Species, Name, Command, BirthDate) VALUES ('Cat', 'Mittens', 'Jump', '2020-06-01');

> INSERT INTO domestic_animals (Species, Name, Command, BirthDate) VALUES > ('Hamster', 'Chewie', 'Run', '2022-05-01');

# Добавление данных в таблицу farm_animals

> INSERT INTO farm_animals (Species, Name, Command, BirthDate) VALUES ('Horse', 'Thunder', 'Gallop', '2019-07-01');

> INSERT INTO farm_animals (Species, Name, Command, BirthDate) VALUES ('Camel', 'Sandy', 'Walk', '2018-03-01');

> INSERT INTO farm_animals (Species, Name, Command, BirthDate) VALUES ('Donkey', 'Bray', 'Carry', '2017-10-01');

# Удаление верблюда из таблицы, в связи с переводом в другой питомник

> DELETE FROM farm_animals WHERE Species = 'Camel';

# Операция "Молодняк". Выборка всех молодых животных и запись в новую таблицу:

> ```CREATE TABLE``` young_animals (
>    ID INT PRIMARY KEY AUTO_INCREMENT,
>    Species VARCHAR(100),
>    Name VARCHAR(100),
>    Command VARCHAR(100),
>    BirthDate DATE,
>    AgeInMonths INT
> );

>```INSERT INTO``` young_animals (Species, Name, Command, BirthDate, AgeInMonths)
>```SELECT``` 
>    Species, 
>    Name, 
>    Command, 
>    BirthDate, 
>    TIMESTAMPDIFF(MONTH, BirthDate, CURDATE()) ```AS``` AgeInMonths 
>```FROM``` 
>    (
>        ```SELECT``` * FROM domestic_animals
>        ```UNION ALL```
>        ```SELECT``` * FROM farm_animals
>    ) ```AS``` animals 
>```WHERE``` 
>    TIMESTAMPDIFF(YEAR, BirthDate, CURDATE()) > 1 AND
>    TIMESTAMPDIFF(YEAR, BirthDate, CURDATE()) < 3;

**Такой запрос выберет всех животных старше 1 года, но младше 3 лет из таблиц domestic_animals и farm_animals, посчитает их возраст в месяцах и добавит эти данные в новую таблицу young_animals.

# Объединение всех таблиц с сохранение принадлежности
> ```CREATE TABLE``` all_animals (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Species VARCHAR(100),
    Name VARCHAR(100),
    Command VARCHAR(100),
    BirthDate DATE,
    AgeInMonths INT,
    SourceTable VARCHAR(100)
);

> ```INSERT INTO``` all_animals (Species, Name, Command, BirthDate, AgeInMonths, SourceTable)
```SELECT``` 
    Species, 
    Name, 
    Command, 
    BirthDate, 
    TIMESTAMPDIFF(MONTH, BirthDate, CURDATE()), 
    'domestic_animals'
```FROM``` domestic_animals
```UNION ALL```
```SELECT``` 
    Species, 
    Name, 
    Command, 
    BirthDate, 
    TIMESTAMPDIFF(MONTH, BirthDate, CURDATE()), 
    'farm_animals'
```FROM``` farm_animals
```UNION ALL```
```SELECT``` 
    Species, 
    Name, 
    Command, 
    BirthDate, 
    AgeInMonths, 
    'young_animals'
```FROM``` young_animals;

** Таким образом, в новой таблице all_animals будет сохранена информация о том, из какой исходной таблицы была получена каждая запись.


#Процесс разработки приложения и его описание:
1. Приложение имеет консольно-текстовый интерфейс
2. Добавлены файлы проекта приложения:
> * _ _init_ _.py - инициация модуля, загрузка переменных окружения
>* main.py - Основной файл, контроллер
>* db.py - файл, включающий в себя все процедуры и SQL запросы, используемые в работе приложения

3. Написан код, запускающий программу, которая проверяет наличие Бд, в случае его отсутствия, создает, и пробует подключиться к ней. В случае успешного подключения, создает две таблицы. и закрывает подключение.
> ```Main.py started```

> ```Database type: sqlite```

> ```Database file path: db\master.db```

> ```Environment loaded successful```

> ```Successfully connected to SQLite database master.db```

> ```Successfully connected to SQLite database master.db```

> ```Database setup completed successfully```

> ```SQLite connection is closed```


* Проект спроектирован для работы как на Windows так и на Linux.
Работосопобность проверена, осталось довести для идеального технического исполнения и 100% функционирования всех модулей проекта.

* Добавлены функции проверки вводимых данных.
*Проект готов

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





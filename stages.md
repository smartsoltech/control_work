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

* создание таблиц:

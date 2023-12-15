# book-manager
Приложение для управления книгами в библиотеке, книги можно создавать,
редактировать, удалять.
Пользователь может получить токен, изменить свой пароль или
восстановить его по почте.

Так же создана динамическая документация адрес указан ниже.


Стек технологий Python 3.8, Django, DRF, SQLite3, drf_yasg

Чтобы запустить проект на данном этапе

* Форкните и клонируйте репозиторий:

```
https://github.com/YuliyaKryuchkova/book-manager```
```

* Cоздать и активировать виртуальное окружение:

* Если у вас Linux/macOS


```
python3 -m venv env
```

```
source env/bin/activate
```

* Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

* Выполнить миграции:

```
python3 manage.py migrate
```

* Создать суперюзера:

```
python3 manage.py createsuperuser
```

* Запустить проект локально:

```
python3 manage.py runserver
```

* Если у вас windows

* Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/scripts/activate
```

* Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

* Выполнить миграции:

```
python manage.py migrate
```

* Создать суперюзера:

```
python manage.py createsuperuser
```

* Запустить проект локально:

```
python manage.py runserver
```
* Создайте папку .env, перенесите
в нее список (указав свои данные) из файла .env.example

* Адрес админки:

/admin/

* Адрес API:

/api/

* Адрес документации:
/redoc/


Автор проекта:

Юлия Крючкова

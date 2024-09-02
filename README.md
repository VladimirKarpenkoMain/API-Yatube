# API Yatube
## Описание
Данное API предназначено для проекта социальной сети Yatube. Позволяет работать с постами, комментариями к постам, группами, подписками, auth-jwt.
## Технологии
* Python 3.11
* Django 3.2
* Django Rest Framework 3.12.4
* Simple JWT 4.7.2
* SQLite3
## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/VladimirKarpenkoMain/API-Yatube.git
```

```
cd API-Yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
## Документация к API доступна по адресу http://127.0.0.1:8000/redoc/ после запуска сервера с проектом

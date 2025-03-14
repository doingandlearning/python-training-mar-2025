# Getting setup 

```bash
django-admin startproject edinburgh
cd edinburgh
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
(http://127.0.0.1:8000/admin)
python manage.py startapp api
```

## Making and applying migrations

Do this when you update or add a model.

```bash
python manage.py makemigrations
python manage.py migrate
```

## Start the server

```bash
python manage.py runserver
```

## Create a new app

```bash
python manage.py startapp <name_of_app>
```
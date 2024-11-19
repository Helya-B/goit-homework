## Як запустити проект
### Крок 1:
``
docker compose up -d
``
### Крок 2:
``
python manage.py migrate
``
### Крок 3:
``
python manage.py seed
``

### Крок 4:
``
python manage.py runserver
``
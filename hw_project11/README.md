## Як запустити проект
### Крок 1:
``
docker compose up -d
``
### Крок 2:
``
alembic upgrade head
``
### Крок 3:
``
uvicorn main:app --host localhost --port 8000 --reload
``
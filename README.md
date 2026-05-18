# Random People Database

Веб-приложение для работы с базой случайных пользователей, загружаемых из внешнего API [randomdatatools.ru](https://randomdatatools.ru).

## Стек технологий

### Backend
- **FastAPI**
- **SQLAlchemy 2.0**
- **PostgreSQL 15**
- **Alembic**
- **Pydantic v2**

### Frontend
- **React 18**
- **Nginx**

### Тестирование
- **Pytest** + **pytest-asyncio** + **pytest-cov**
- Unit-тесты (моки БД и API)
- Интеграционные тесты (SQLite в памяти)

## Быстрый запуск (Docker)

### Клонировать репозиторий
git clone https://github.com/Konstanta202/Yadro_test.git

### Запустить все сервисы
docker-compose up --build

Приложение будет доступно:

Фронтенд: http://localhost:3000
Backend API: http://localhost:8000
Swagger: http://localhost:8000/docs
При первом запуске автоматически загружается 1000 случайных пользователей.


## Для локальной разработки 

### используется .env (порт БД 5440 проброшен из Docker):

DB_HOST=localhost
DB_PORT=5440
DB_USER=postgres
DB_PASS=1111
DB_NAME=test_task_db
COUNT_USERS_INIT=1000

### Для Docker используется .env.docker (хост database — имя сервиса):

DB_HOST=database
DB_PORT=5432
DB_USER=postgres
DB_PASS=1111
DB_NAME=test_task_db
COUNT_USERS_INIT=1000

## Миграции (через uv)

bash
### Создать миграцию
uv run alembic revision --autogenerate -m "описание"

### Применить
uv run alembic upgrade head

### Откатить
uv run alembic downgrade -1


## Тестирование

Общее покрытие: **73%** (21 тест)

### Запуск тестов

#### Все тесты с покрытием
uv run pytest tests/ --cov=app --cov-report=term-missing

#### Только модульные
uv run pytest tests/unit/ -v

#### Только интеграционные
uv run pytest tests/integration/ -v -m integration

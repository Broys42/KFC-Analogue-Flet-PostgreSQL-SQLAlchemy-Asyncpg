# KFC_Analogue (Flet, PostgreSQL, SQLAlchemy, Asyncpg)

## О проекте
- Весь интерфейс написан на Flet
- Данные передаются через ORM-запросы к базе данных PostgreSQL
- ORM-запросы реализованы через SQLAlchemy
- Интерфейс и CRUD операции выполняются ассинхронно

## Что можно делать
- Создание и редактирование карточек меню
- Создание и редактирование карточек пользователей
- Добавление пользователям любимые блюда (o2m) (В разработке)

## Установка
```sh
git clone https://github.com/Broys42/KFC-Analogue-Flet-PostgreSQL-SQLAlchemy-Asyncpg.git
cd KFC-Analogue-Flet-PostgreSQL-SQLAlchemy-Asyncpg
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## .env
```sh
DB_HOST: str
DB_PORT: int
DB_USER: str
DB_PASS: str
DB_NAME: str
CREATE_DB: bool
```

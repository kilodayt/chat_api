# Chat API (Django + DRF + Pydantic)

* **Фреймворк:** Django >=4.2 + DRF
* **Валидация:** Pydantic v2
* **База данных:** PostgreSQL 15
* **Документация:** drf-spectacular
* **Тестирование:** Pytest-django
* **Контейнеризация:** Docker, Docker Compose

## Запуск проекта

Скопируйте репозиторий.

```bash
git clone https://github.com/kilodayt/chat_api
```

Перед запуском создайте файл `.env` в корне проекта.

```bash
cp .env.example .env
```

Выполните команду в корневой директории:

```bash
docker-compose up --build
```

## Запуск тестов

Для запуска тестов в контейнере введите команду:

```bash
docker-compose exec web pytest
```

## Основные эндпоинты

| Метод | Эндпоинт | Описание                                      |
| :--- | :--- |:-----------------------------------------------|
| `POST` | `/chats/` | **Создать новый чат**               |
| `GET` | `/chats/{id}/` | **Детали чата**                   |
| `POST` | `/chats/{id}/messages/` | **Отправить сообщение**   |
| `DELETE` | `/chats/{id}/` | **Удалить чат вместе с сообщениями**.


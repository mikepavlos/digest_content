# digest_content
### Упрощенный микросервис для подготовки дайджестов контента

Микросервис получает запрос от основного приложения на подготовку контента постов. 
Возвращает подготовленный дайджест наиболее популярных постов от каждого источника, на которые подписан пользователь.  

### Стек
- python 3.11.2
- FastAPI 0.95.0
- SQLAlchemy 1.4.41
- PostgreSQL 15.1
- Docker

### Запуск проекта в контейнере Docker

Клонировать проект

```commandline
git clone https://github.com/mikepavlos/digest_content.git
```

Создать `.env` файл, либо изменить образец `.env.example` файла в директории проекта, улалив `.example`.  

Запустить контейнеры командой

```commandline
 docker compose up -d --build
```

Endpoint: `app/v1/digests/{user_id}`

Документация к API `app/v1/docs#`

----

### Автор
Михаил Павлов  
https://github.com/mikepavlos
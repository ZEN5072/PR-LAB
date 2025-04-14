# 📦 Lab #3 — ToDo List Web App in Docker 
(Without Docker Compose) EN

## 🎯 Goal of the Lab

Build a full-featured **ToDo List web application** using REST API and a 3-container architecture:

- ✅ View tasks
- ✅ Add new tasks
- ✅ Edit tasks
- ✅ Delete tasks
- ✅ Toggle task completion
- ✅ View task details by ID

All components must run in **separate Docker containers**, connected using a **custom Docker network**, **not** using `docker-compose`.

---

## 🧠 Theoretical Overview

### 🔹 Docker Network Principle

Docker networks allow containers to communicate via container names. Once a network is created:

```bash
docker network create todo-net-lab3
```

All containers connected to that network can resolve each other by name, like `http://backend-lab3:8000`.

---

## 🧱 Application Architecture

```
[Browser] → localhost:8080 → [Frontend (Nginx + HTML + JS)]
                                 |
                                 ▼
                      http://localhost:8000 → [Backend (FastAPI)]
                                                        |
                                                        ▼
                                            [PostgreSQL Database]
```

---

## 🧪 Project Structure

```
todo-lab3/
├── backend/       # FastAPI + SQLAlchemy + Pydantic
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── Dockerfile
├── frontend/      # HTML + JS + Nginx
│   ├── index.html
│   └── Dockerfile
├── db/            # PostgreSQL base image
│   └── Dockerfile
└── README.md
```

---

## 🏗 Step-by-Step Execution

### 🔸 1. PostgreSQL Database

**Dockerfile (`db/Dockerfile`):**

```dockerfile
FROM postgres:14
ENV POSTGRES_USER=todo
ENV POSTGRES_PASSWORD=todo
ENV POSTGRES_DB=todo_db
```

**Build and run:**

```bash
docker build -t todo-db-lab3 ./db
docker run -d --name db-lab3 --network todo-net-lab3 todo-db-lab3
```

---

### 🔸 2. Backend (FastAPI)

**Dockerfile (`backend/Dockerfile`):**

```dockerfile
FROM python:3.11
WORKDIR /app
COPY . /app
RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Key points:**

- FastAPI used for REST API
- SQLAlchemy manages the database
- Pydantic handles schema validation
- CORS middleware is enabled

**Build and run:**

```bash
docker build -t todo-backend-lab3 ./backend
docker run -d --name backend-lab3 --network todo-net-lab3 -p 8000:8000 todo-backend-lab3
```

---

### 🔸 3. Frontend (HTML + JS + Nginx)

**Dockerfile (`frontend/Dockerfile`):**

```dockerfile
FROM nginx:alpine
COPY ./index.html /usr/share/nginx/html/index.html
```

**index.html** includes:
- Adding tasks
- Editing titles
- Deleting tasks
- Toggling completion
- Dynamically loads list via `fetch()`

**Build and run:**

```bash
docker build -t todo-frontend-lab3 ./frontend
docker run -d --name frontend-lab3 --network todo-net-lab3 -p 8080:80 todo-frontend-lab3
```

---

## 🧪 Testing

Open your browser and go to:

```
http://localhost:8080
```

- Add some tasks
- Try editing them (via prompt)
- Toggle completion status
- Delete tasks

Make sure API requests (`GET`, `POST`, `PUT`, `DELETE`) are being made correctly via browser DevTools → Network tab.

---

## 🛠 Useful Docker Commands

```bash
# List containers
docker ps

# Inspect network
docker network inspect todo-net-lab3

# Logs from container
docker logs backend-lab3
```

---

## 📸 Screenshots (to add in report)

- Working UI in browser
- List of tasks
- DevTools → Network panel (showing API calls)
- Terminal output of `docker ps`
- Network inspection

---

## 📦 Conclusion

✅ Successfully built a full CRUD ToDo List application  
✅ Split into frontend (HTML/JS), backend (FastAPI), and database (PostgreSQL)  
✅ All components run in **isolated Docker containers**  
✅ **No `docker-compose` used** — pure Docker CLI  
✅ REST API is clean and documented via `/docs`  
✅ Frontend interacts with backend via `fetch()` and dynamic UI

---

## 🔗 Repo

`https://github.com/ZEN5072/PR-LAB`

---

## 📚 University & Course Info

This project was developed as part of **Laboratory Work #3**  
📌 **PR (Programarea Rețelelor)** course  
🏛 **UTM — Technical University of Moldova**  
🎓 **FCIM Faculty — Faculty of Computers, Informatics, and Microelectronics**

If you're from **UTM / FCIM** and reviewing this repo — welcome!  
This is a complete solution fully aligned with the course requirements (PR).


---
---


# 📦 Лабораторная работа №3 — ToDo List в Docker 
(без Docker Compose) RU

## 🧾 Цель работы

Создать веб-приложение **ToDo List** с полным CRUD:

- Просмотр всех задач
- Добавление новой задачи
- Редактирование задачи
- Удаление задачи
- Изменение статуса "выполнено"
- Получение задачи по ID

Всё должно работать через **REST API** и запускаться через **три отдельных Docker-контейнера**:
- `frontend` — HTML+JS интерфейс
- `backend` — FastAPI (Python)
- `db` — PostgreSQL

> **Без использования `docker-compose`. Только через `docker network`.**

---

## 🧠 Теоретическая часть

### 🔹 Принцип работы Docker Network

Docker позволяет создавать изолированные виртуальные сети, в которых контейнеры могут находить друг друга по имени. Это даёт возможность настроить связь между frontend, backend и базой данных без проброса внутренних IP.

```bash
docker network create todo-net-lab3
```

---

## 🧱 Архитектура приложения

```
[Browser] → localhost:8080 → [Frontend (nginx)]
                                 |
                                 ▼
                       http://localhost:8000 → [Backend (FastAPI)]
                                                        |
                                                        ▼
                                            [PostgreSQL Database]
```

---

## 🏗 Ход выполнения

### 🔸 1. База данных (PostgreSQL)

**Dockerfile (db/Dockerfile):**

```dockerfile
FROM postgres:14
ENV POSTGRES_USER=todo
ENV POSTGRES_PASSWORD=todo
ENV POSTGRES_DB=todo_db
```

**Сборка и запуск:**

```bash
docker build -t todo-db-lab3 ./db
docker run -d --name db-lab3 --network todo-net-lab3 todo-db-lab3
```

---

### 🔸 2. Backend (FastAPI + SQLAlchemy)

**Dockerfile (backend/Dockerfile):**

```dockerfile
FROM python:3.11
WORKDIR /app
COPY . /app
RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**main.py** включает CORS, маршруты и работу с базой.

**Сборка и запуск:**

```bash
docker build -t todo-backend-lab3 ./backend
docker run -d --name backend-lab3 --network todo-net-lab3 -p 8000:8000 todo-backend-lab3
```

---

### 🔸 3. Frontend (Nginx + HTML/JS)

**Dockerfile (frontend/Dockerfile):**

```dockerfile
FROM nginx:alpine
COPY ./index.html /usr/share/nginx/html/index.html
```

**index.html** реализует:
- список задач
- добавление
- редактирование
- удаление
- переключение "выполнено"

**Сборка и запуск:**

```bash
docker build -t todo-frontend-lab3 ./frontend
docker run -d --name frontend-lab3 --network todo-net-lab3 -p 8080:80 todo-frontend-lab3
```

---

## 🧪 Проверка

- Открыть в браузере: [http://localhost:8080](http://localhost:8080)
- Проверить `GET`, `POST`, `PUT`, `DELETE` запросы через DevTools (или через `/docs`)
- Проверить, что все контейнеры находятся в сети:

```bash
docker network inspect todo-net-lab3
```

---

## 📸 Скриншоты (пример)

Добавь сюда:

- Интерфейс в браузере
- Список задач
- Удаление/редактирование в действии
- `docker ps`
- `docker network inspect`

---

## 📦 Выводы

✅ Создано клиент-серверное ToDo-приложение с полной реализацией CRUD.  
✅ Использована архитектура **frontend ↔ backend ↔ database**, разнесённая по **трём Docker-контейнерам**.  
✅ Использована **docker network** вместо Compose.  
✅ Реализован REST API с помощью **FastAPI**.  
✅ Взаимодействие frontend с API работает через `fetch()` и CORS.

---

## 🔗 Репозиторий

`https://github.com/ZEN5072/PR-LAB`

_(добавь ссылку на GitHub, если нужен шаблон — могу сделать)_




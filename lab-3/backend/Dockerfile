FROM python:3.11
WORKDIR /app
COPY . /app
RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

#   docker build -t todo-backend-lab3 ./backend
#   docker run -d --name backend --network todo-net -p 8000:8000 todo-backend

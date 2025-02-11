# Используем официальный образ Python
FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /lab1

# Копируем файлы в контейнер
COPY requirements.txt requirements.txt
COPY lab_1.py lab_1.py

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Запускаем приложение
CMD ["python", "lab_1.py"]

#студент не смог, чат помог
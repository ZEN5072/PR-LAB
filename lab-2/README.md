# Лабораторная работа №2: Создание и взаимодействие двух REST API приложений

## Цель работы
Понять принципы REST и научиться создавать приложения, взаимодействующие через HTTP.

## Описание
Проект состоит из двух Flask-приложений:
1. Server - основное приложение с хранилищем данных
2. Client - приложение для взаимодействия с сервером

## Установка и запуск

# Сборка Docker-образов:
```bash
cd server

docker build -t server-app .

cd ../client 

docker build -t client-app .
```
  
  
  
  
***  
***  
  
  
  
  
  
  
# Выполнение лабораторной работы №2

### Создание сети:
```bash
docker network create lab2-network
```

### Запуск контейнеров:
```bash
docker run -d --name server --network lab2-network -p 5000:5000 server-app

docker run -d --name client --network lab2-network -p 5001:5001 client-app
```

## Тестирование с помощью curl

### Создание элемента:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name":"test","description":"test desc"}' http://localhost:5001/items
```

### Получение всех элементов:
```bash
curl http://localhost:5001/items
```

### Обновление элемента:
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name":"updated"}' http://localhost:5001/items/1
```

### Удаление элемента:
```bash
curl -X DELETE http://localhost:5001/items/1
```

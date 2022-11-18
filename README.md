# Collector - сбор статистики погоды по городам.

Данный модуль собирает статистику актуальной температуры по городам с сайта https://openweathermap.org/

При желании приложение можно расширить дла сбора актуальной информации:
-о ветре 
Например, для ипользования ветрегонераторов и предсказания их мощности или определение опасности шторма.
Об облочности, 
для определения условий работы солнечных батарей, управлением уровня освещения
Об времени воссхода и заката солна
для определения времени автоматического включения дополнительного освещения.


## Подготовка и запуск проекта
### Склонировать репозиторий на локальную машину:
```
git clone https://github.com/MariyaAnis/statistics-collector
```
## Для работы (на ubuntu):


* Установите docker на сервер:
```
sudo apt install docker.io 
```
* Установите docker-compose:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

* Cоздайте .env файл и впишите:
    ```
    DB_ENGINE=<django.db.backends.postgresql>
    DB_NAME=<имя базы данных postgres>
    DB_USER=<пользователь бд>
    DB_PASSWORD=<пароль>
    DB_HOST=<collector>
    DB_PORT=<5432>
    SECRET_KEY=<секретный ключ проекта django>
    
    API_KEY=<Ключ с сайта https://openweathermap.org/>
  
  
    ```

* Запустите docker-compose:
```
sudo docker-compose up -d --build
```
* После успешной сборки выполните команды:
    - Соберите статические файлы:
    ```
    sudo docker-compose exec backend python manage.py collectstatic --noinput
    ```
    - Примените миграции:
    ```
    sudo docker-compose exec backend python manage.py migrate --noinput
    ```
    - Загрузите города  в базу данных (необязательно):
    ```
    sudo docker-compose exec backend python manage.py load_ingredients <Название файла из директории data>
    ```
    - Создать суперпользователя Django:
    ```
    sudo docker-compose exec backend python manage.py createsuperuser
    ```
    - Проект будет доступен по вашему IP
  
# Ватник

## Структура базы

| Текст сообщения | id сообщения | id юзера | Имя юзера | Дата отправки сообщения |
| --------------- | ------------ | -------- | --------- | ----------------------- |
|                 |              |          |           |                         |
|                 |              |          |           |                         |
|                 |              |          |           |                         |

Не все из этого используется, но возможно в будующем заюзаю.

## Как запустить

В [launch.bat](launch.bat) надо выставить переменные окружения (токен и путь до бд)

Потом
```
> python -m virtualenv .
> Scripts\activate.bat
> pip install -r requirements.txt
> launch.bat
```


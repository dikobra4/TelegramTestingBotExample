# Пример тестового бота Telegram

Репозиторий с примером тестового бота Telegram для [статьи на Хабр](https://habr.com/ru/post/723342/)

## Запуск
1. Пройти регистрацию приложения на [my.telegram.org](https://my.telegram.org/)
2. Установить необходимые библиотеки из requirements
3. Запустить redis-server
4. Заполнить файл .env необходимыми данными
5. Запустить скрипт t_bot.py (при первом запуске нужно будет ввести телефон и код)

После этого можно запускать тесты

## Файл .env
1. API_ID - API ID сгенерированный на [my.telegram.org](https://my.telegram.org/)
2. API_HASH - API HASH сгенерированный на [my.telegram.org](https://my.telegram.org/)
3. SESSION_NAME - имя файла сессии, который сгенерируется при первом запуске t_bot.py
4. BOT_FOR_TEST_NAME - username бота, которого мы будем тестировать в telegram
5. REDIS_HOST - ip хоста Redis (по умолчанию localhost)
6. REDIS_PORT - порт хоста Redis (по умолчанию 6379)
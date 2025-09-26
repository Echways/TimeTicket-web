
# TimeTicket Web

![Django](https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/DB-SQLite-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

---

## О проекте

>**TimeTicket** — веб-приложение, реализованное на Django.  
>Проект содержит приложение `main` и использует стандартную SQLite базу данных для разработки. В репозитории присутствуют медиа-файлы (папка `media` с изображениями) и шаблоны/статические ресурсы.
---

## Ключевые особенности
- Реализовано Django-приложение.
- Поддержка media-файлов (загружаемые изображения).
- Простой старт на SQLite для локальной разработки.

---

## Технологии
- Python 3.10+  
- Django  
- SQLite
- HTML/CSS шаблоны и статические файлы  

---

## Быстрая установка (локально)

1. Клонируйте репозиторий:
```bash
git clone git@github.com:Echways/TimeTicket-web.git
cd timeticket-web
```

2. Создайте виртуальное окружение и активируйте:
```bash
python3 -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows (PowerShell)
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Настройте переменные окружения (опционально):
Создайте `.env` в корне проекта:
```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

5. Выполните миграции и создайте суперпользователя:
```bash
python manage.py migrate
python manage.py createsuperuser
```

6. Запустите локальный сервер:
```bash
python manage.py runserver
# или: python manage.py runserver 0.0.0.0:8000
```

7. Откройте в браузере: `http://127.0.0.1:8000/`
---

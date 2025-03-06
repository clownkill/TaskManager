# TaskManager

## 📌 О проекте
**TaskManager** — это простое Django-приложение для работы с задачами.


### Методы API

#### 1. **Создать задачу**

**Эндпоинт:** `/tasks/`

**Метод:** `POST`

**Описание:** Создание задачи.

#### Пример запроса:
```json
{
  "title": "Тестовая задача"
}
```
**items:** Список ID товаров, которые были приобретены в чеке.
**is_completed** Статус исполнения задачи (необязательный параметр. По умолчанию - False)

#### Пример ответа:
```json
{
  "title": "Тестовая задача",
  "is_completed": false
}
```

#### 2. **Получить список задач**

**Эндпоинт:** `/tasks/`

**Метод:** `GET`

**Описание:** Получение списка задач.

#### Пример ответа:
```json
[
  {
    "title": "Тестовая задача 1",
    "is_completed": false
  },
  {
    "title": "Тестовая задача 2",
    "is_completed": false
  },
  {
    "title": "Тестовая задача 3",
    "is_completed": true
  }
]
```

## 🚀 Запуск проекта

### 1️⃣ Клонирование репозитория
```sh
git clone <URL_РЕПОЗИТОРИЯ>
cd TASKMANAGER
```

### 2️⃣ Создание виртуального окружения, установка зависимостей и установка pre-commit hooks
```sh
python -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate    # Для Windows
pip install -r requirements.txt
```

### 3️⃣ Создание `.env` файла
Создайте файл `.env` на основе `.env.example`:
```sh
cp .env.example .env
```
Заполните переменные в `.env`.

### 4️⃣ Применение миграций и создание суперпользователя
```sh
python manage.py migrate
python manage.py createsuperuser
```
Заполните данные (email, пароль) и подтвердите.

### 5️⃣ Запуск проекта
```sh
python manage.py runserver
```
# Django-Store

Учебный проект по Djanga

### Окружение

- Python 3.7^
- Postgresql 11^
- бд store_db (по умолчанию нужен логин пароль postgres postgres, настраивается в store/settings.py)

## Установка
1. Виртуальное окружение
```
python -m venv venv
venv/Scripts/activate.bat
```
2. Установка пакетов
```
pip install -r requirements.txt
```
3. Миграции
```
python manage.py migrate
python manage.py loaddata <path_to_fixture_files>
```
4. Запуск
```
python manage.py runserver
```
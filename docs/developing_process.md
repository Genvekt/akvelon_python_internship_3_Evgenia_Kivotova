# Notes about development steps.
Here I capture main development steps and decisions for future me.

## Project setup and architecture
1. Create GitHub repo with README, python gitignore and clone it
2. Create venv and activate with 

```
python3 -m venv finance_manager_env
source finance_manager_env/bin/activate
```
3. `pip install Django`
4. Start project with `django-admin startproject finance_site`

## Application setup
1. Create application with `python manage.py startapp finance_manager`
2. Register application in `finance_site/settings.py`, adding `'finance_manager.apps.FinanceManagerConfig'` to `INSTALLED_APPS`

## App view setup
1. Create view endpoints at `finance_manager.views.py`
2. Create routing manager `finance_manager.urls.py`
3. Register views from `finance_manager.views.py` in routing manager `finance_manager.urls.py`
2. Requster routing manager in `finance_site/urls.py` by adding `path('finance_manager/', include('finance_manager.urls'))` to `urlpatterns`. This will make application more independent from finance_site project, so that it can be removed easily.

## Dockerize application

. Setup the database in project settings `settings.py`
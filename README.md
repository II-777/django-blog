# Django Blog

## Part 1 - Getting Started
```bash
# create and start python3 virtual environment 
python3 -m venv .venv
source .venv/bin/activate
# install required python3 modules 
pip install -r requirements.txt
# create a django project
django-admin startproject django_project
```

### The `startproject` command cretes the following django file structure:
	- new file:   django_project/__init__.py
	- new file:   django_project/settings.py
	- new file:   django_project/urls.py
	- new file:   django_project/wsgi.py
	- new file:   manage.py
	- new file:   db.sqlite3

1. **`django_project/__init__.py`:**
   - This file is an empty Python script that tells Python that the directory should be considered a Python package. It is typically left blank unless you have specific initialization code for the package.
2. **`django_project/settings.py`:**
   - The primary configuration file for a Django project, containing settings such as database configuration, static files, middleware, and other project-specific configurations.
3. **`django_project/urls.py`:**
   - Defines the URL patterns for the project, mapping URLs to views. It serves as the central routing mechanism for directing incoming requests to the appropriate view functions.
4. **`django_project/wsgi.py`:**
   - Stands for Web Server Gateway Interface. This file serves as an entry point for the WSGI server to interact with your Django application, enabling it to be deployed on production servers.
5. **`manage.py`:**
   - A command-line utility that provides various tools for interacting with and managing a Django project, including running development servers, creating database tables, and handling migrations.
6. **`db.sqlite3`:**
   - The default SQLite database file created by Django when you run migrations. It stores the project's data, including tables for models defined in the project's apps. This file is part of the default configuration and can be replaced with other database backends as needed.

## Part 2 - Applications and Routes

## Part 3 - Templates

## Part 4 - Admin Page

## Part 5 - Database and Migrations

## Part 6 - User Registration

## Part 7 - Login and Logout System

## Part 8 - User Profile and Picture

## Part 9 - Update User Profile

## Part 10 - Create, Update, and Delete Posts

## Part 11 - Pagination

## Part 12 - Email and Password Reset
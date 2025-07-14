# Task Management API

This project provides a small Django REST backend for collaborative task management.

## Features
- JWT authentication (register, login, current user)
- CRUD operations for tasks
- PostgreSQL with Django ORM
- CORS enabled for local Angular frontend

## Setup
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and update the values for the database and secret key.
3. Apply migrations and run the application:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

The database tables are created automatically with Django migrations.

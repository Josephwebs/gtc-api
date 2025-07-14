# Task Management API (Flask)

This project provides a simple Flask backend for collaborative task management.
It uses JWT authentication, PostgreSQL via SQLAlchemy and is ready for
integration with an Angular frontend.

## Features
* User registration and login with JWT
* CRUD operations for tasks
* PostgreSQL with Flask-Migrate migrations
* CORS enabled for `http://localhost:4200`

## Setup
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` inside the `backend` folder and update values.
3. Run database migrations:
   ```bash
   flask --app backend.main db init   # first time only
   flask --app backend.main db migrate -m "init"
   flask --app backend.main db upgrade
   ```
4. Start the server:
   ```bash
   flask --app backend.main run --debug
   ```

## Example usage with `curl`
Register:
```bash
curl -X POST http://localhost:5000/register \
  -H 'Content-Type: application/json' \
  -d '{"username":"user","email":"user@example.com","password":"secret"}'
```
Login:
```bash
curl -X POST http://localhost:5000/login \
  -H 'Content-Type: application/json' \
  -d '{"username":"user","password":"secret"}'
```
Use the returned token for further requests:
```bash
TOKEN=... # from login response
curl -H "Authorization: Bearer $TOKEN" http://localhost:5000/me
```

Create a task:
```bash
curl -X POST http://localhost:5000/tasks/ \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"title":"My task","description":"Something to do"}'
```

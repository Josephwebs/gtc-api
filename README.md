# Task Management API

This project provides a small FastAPI backend for collaborative task management.

## Features
- JWT authentication (register, login, current user)
- CRUD operations for tasks
- PostgreSQL with SQLAlchemy
- CORS enabled for local Angular frontend

## Setup
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and update the values.
3. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

The database tables are created automatically on startup using SQLAlchemy metadata.

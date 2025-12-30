# Todo App FastAPI Service

Welcome to the **Todo App FastAPI Service**! This project is a simple, robust RESTful API for managing Todos, built with [FastAPI](https://fastapi.tiangolo.com/). It features reusable response message utilities, modular routing, and a focus on clean architecture.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Setup & Installation](#setup--installation)
- [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)
- [Development Info](#development-info)

---

## Project Structure

```
.
├── src/
│   ├── api/
│   │   └── v1/
│   │       └── routes/
│   │           └── todo_routes.py        # API endpoints for Todos
│   ├── database/
│   │   └── db.py                         # Database session and setup
│   ├── models/
│   │   └── todo.py                       # SQLModel for Todo item
│   ├── server.py                         # FastAPI app entrypoint
│   ├── utils/
│   │   └── generate_response_messages.py # Utility for consistent API responses
│   └── ...
├── static/                               # Static files (e.g., favicon)
├── README.md
└── ...
```

---

## Features

- **RESTful Todo API**: Create, retrieve, update, and delete tasks.
- **Automatic Documentation**: Swagger UI available at `/docs`.
- **Modular Structure**: Separation of API, database, models, and utilities for maintainability.
- **Reusable Response Messages**: Centralized error and response message logic.
- **Environment Config Friendly**: Set the database URL through environment variables.

---

## Setup & Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. **Create a virtual environment and activate it**

   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```
   pip install -r requirements.txt
   ```

4. **Set up your environment**

   Create a `.env` file or set the `DATABASE_URL` environment variable (e.g., for SQLite):

   ```
   DATABASE_URL=sqlite:///./todos.db
   ```

---

## Running the Server

From the `src/` directory (or project root if properly structured), run:

```bash
uvicorn server:app --reload
```

- The server starts at [http://localhost:8000](http://localhost:8000)
- Swagger docs (with custom favicon): [http://localhost:8000/docs](http://localhost:8000/docs)

---

## API Endpoints

- `GET /todos/` — List todos
- `GET /todos/{todo_id}` — Retrieve a specific todo
- `POST /todos/` — Create a new todo
- `PUT /todos/{todo_id}` — Update an existing todo
- `DELETE /todos/{todo_id}` — Delete a todo

**Response messages for errors are consistent and informative, thanks to the utility in `utils/generate_response_messages.py`.**

---

## Development Info

- **Main entry point:** `src/server.py`
- **Utilities:** Error/response mapping in `src/utils/generate_response_messages.py`
- **Database setup:** Created at app startup; see `create_db_and_tables()` in `database/db.py`
- **Static files:** Served from `static/` (used for custom Swagger favicon).

---

## Requirements

- Python 3.10+
- FastAPI
- SQLModel
- Uvicorn

(See `requirements.txt` for a complete list)

---

## License

MIT License

---

## Notes

- The project is ready for extension: add authentication, validation, or other features as needed!
- For any questions or suggestions, open an issue or pull request.

Happy coding! 🚀

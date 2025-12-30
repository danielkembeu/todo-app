from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html

from api.v1.routes import todo_routes as tr
from database.db import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        print(app)
        create_db_and_tables()
        print("Database started successfully !")
    except e:
        print(f"[DATABASE_INIT_ERROR]: {e}")
    yield


app = FastAPI(lifespan=lifespan, title="Todo App Service",
              swagger_favicon_url="/favicon.webp", version="1.0.0")

# app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(tr.router)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Documentation",
        swagger_favicon_url="/static/favicon.webp"  # Votre favicon local
    )

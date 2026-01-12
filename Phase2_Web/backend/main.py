from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import create_engine, SQLModel

from backend.core.config import settings
from backend.api.endpoints import tasks, auth

app = FastAPI(
    title="Todo App",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS
origins = []
if settings.BACKEND_CORS_ORIGINS:
    origins = [str(origin).strip() for origin in settings.BACKEND_CORS_ORIGINS.split(",")]

print(f"CORS origins configured: {origins}") # Debug print

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
    allow_headers=["*"],
)

engine = create_engine(settings.DATABASE_URL, echo=True)

from sqlalchemy.exc import OperationalError # Import OperationalError

# ... existing code ...

@app.on_event("startup")
def on_startup():
    try:
        SQLModel.metadata.create_all(engine)
    except OperationalError as e:
        print(f"ERROR: Could not connect to database on startup. Please ensure the database is running and accessible. Error: {e}")
        # Optionally, you might want to raise the exception or implement a retry mechanism here
        # For now, we'll just log and let the app start, though DB-dependent routes will fail.

app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(tasks.router, prefix=f"{settings.API_V1_STR}", tags=["tasks"])
